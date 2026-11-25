
from backend.schemas import validate_generated_ui
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from ai_engine.prompts import (
    build_ui_prompt,
    build_repair_prompt
)


# Load API key from .env
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found in .env")


# Gemini configuration
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    api_key=api_key,
    timeout=120,
    max_retries=2
)


def extract_text(content):
    """Extract readable text from Gemini response."""

    if isinstance(content, str):
        return content

    if isinstance(content, list):
        text_parts = []

        for block in content:
            if isinstance(block, dict) and block.get("type") == "text":
                text_parts.append(block.get("text", ""))
            elif isinstance(block, str):
                text_parts.append(block)

        return "\n".join(text_parts)

    return str(content)


def test_connection():
    """Test Gemini API connection."""

    print("Connecting to Gemini...")

    try:
        response = llm.invoke(
            "Reply with exactly: AuraGen Gemini connection successful!"
        )

        print("\nGemini response:")
        print(extract_text(response.content))

    except Exception as error:
        print("\nConnection failed:")
        print(type(error).__name__)
        print(str(error)[:1000])


def generate_ui(
    user_request,
    form_context="",
    cognitive_load_score=None
):
    """
    Generate a React component using AuraGen's
    design system and cognitive load score.
    """

    prompt = build_ui_prompt(
        user_request=user_request,
        form_context=form_context,
        cognitive_load_score=cognitive_load_score
    )

    response = llm.invoke(prompt)

    return extract_text(response.content)


def generate_validated_ui(
    user_request,
    form_context="",
    cognitive_load_score=None
):
    """
    Generate React UI using Gemini and validate
    the response using Pydantic.
    """

    # Generate raw React code
    raw_output = generate_ui(
        user_request=user_request,
        form_context=form_context,
        cognitive_load_score=cognitive_load_score
    )

    # Validate the AI-generated response
    validated_response = validate_generated_ui(raw_output)

    return validated_response


if __name__ == "__main__":

    test_connection()

    print("\nGenerating AuraGen UI...")

    try:
        generated_code = generate_ui(
            user_request="Simplify the financial form into smaller steps.",
            form_context=(
                "The form contains name, email "
                "and monthly income."
            ),
            cognitive_load_score=85
        )

        print("\nGenerated React Component:\n")
        print(generated_code)

    except Exception as error:
        print("\nGeneration failed:")
        print(type(error).__name__)
        print(str(error)[:1000])

def generate_self_healing_ui(
    user_request,
    form_context="",
    cognitive_load_score=None,
    max_repair_attempts=2
):
    """
    Generate React UI, validate it using Pydantic
    and Babel, and repair invalid JSX using Gemini.
    """

    from backend.babel_client import validate_jsx

    # Step 1: Generate initial UI
    raw_output = generate_ui(
        user_request=user_request,
        form_context=form_context,
        cognitive_load_score=cognitive_load_score
    )

    # Step 2: Validate Gemini response using Pydantic
    validated_response = validate_generated_ui(raw_output)

    # Step 3: Validate JSX using Babel
    babel_result = validate_jsx(validated_response.code)

    repair_attempts = 0

    # Step 4: Repair invalid JSX if necessary
    while not babel_result.get("valid") and repair_attempts < max_repair_attempts:

        repair_attempts += 1

        repair_prompt = build_repair_prompt(
            invalid_code=validated_response.code,
            validation_error=babel_result.get("message", "Unknown JSX error"),
            user_request=user_request,
            form_context=form_context,
            cognitive_load_score=cognitive_load_score
        )

        # Ask Gemini to repair the code
        repair_output = extract_text(
            llm.invoke(repair_prompt).content
        )

        # Validate repaired response using Pydantic
        validated_response = validate_generated_ui(repair_output)

        # Validate repaired JSX using Babel
        babel_result = validate_jsx(validated_response.code)

    # Step 5: Return complete result
    return {
        "component_name": validated_response.component_name,
        "language": validated_response.language,
        "code": validated_response.code,
        "explanation": validated_response.explanation,
        "babel_validation": babel_result,
        "self_healed": repair_attempts > 0 and babel_result.get("valid", False),
        "repair_attempts": repair_attempts
    }
