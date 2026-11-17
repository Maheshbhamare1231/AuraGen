
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from ai_engine.prompts import build_ui_prompt

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


def generate_ui(user_request, form_context=""):
    """Generate a React component using AuraGen's design system."""

    prompt = build_ui_prompt(
        user_request=user_request,
        form_context=form_context
    )

    response = llm.invoke(prompt)

    return extract_text(response.content)


if __name__ == "__main__":

    test_connection()

    print("\nGenerating AuraGen UI...")
    
    try:
        generated_code = generate_ui(
            user_request="Simplify the financial form into smaller steps.",
            form_context="The form contains name, email and monthly income."
        )

        print("\nGenerated React Component:\n")
        print(generated_code)

    except Exception as error:
        print("\nGeneration failed:")
        print(type(error).__name__)
        print(str(error)[:1000])
