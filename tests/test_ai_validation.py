from ai_engine.llm import generate_validated_ui


def test_gemini_validation():

    print("Generating React UI with Gemini...")

    try:
        response = generate_validated_ui(
            user_request="Create a simple two-step financial form.",
            form_context="Fields: full name, email and monthly income."
        )

        print("\nValidation successful!")

        print("\nComponent Name:")
        print(response.component_name)

        print("\nLanguage:")
        print(response.language)

        print("\nValidated React Code:")
        print(response.code)

        print("\nExplanation:")
        print(response.explanation)

    except Exception as error:
        print("\nGeneration or validation failed!")

        print("Error Type:", type(error).__name__)
        print("Error:", str(error))


if __name__ == "__main__":
    test_gemini_validation()