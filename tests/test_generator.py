
from pathlib import Path
from ai_engine.llm import generate_ui

# Project folders
PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = PROJECT_ROOT / "generated_components"

OUTPUT_DIR.mkdir(exist_ok=True)

# Three different UI generation scenarios
test_cases = [
    {
        "filename": "FinancialWizard.jsx",
        "request": "Create a two-step financial information form.",
        "context": "Fields: full name, email address and monthly income."
    },
    {
        "filename": "RegistrationForm.jsx",
        "request": "Create a simple user registration form.",
        "context": "Fields: full name, email, password and confirm password."
    },
    {
        "filename": "ContactForm.jsx",
        "request": "Create a clean and accessible contact form.",
        "context": "Fields: name, email, subject and message."
    }
]


def clean_code(code):
    """Remove Markdown code fences if Gemini returns them."""

    code = code.strip()

    if code.startswith("```"):
        lines = code.splitlines()

        if lines[-1].strip() == "```":
            lines = lines[1:-1]

        code = "\n".join(lines)

    return code.strip()


def run_generation_tests():

    for index, test in enumerate(test_cases, start=1):

        print("\n" + "=" * 50)
        print(f"TEST {index}: {test['filename']}")
        print("=" * 50)

        try:
            generated_code = generate_ui(
                user_request=test["request"],
                form_context=test["context"]
            )

            generated_code = clean_code(generated_code)

            output_file = OUTPUT_DIR / test["filename"]
            output_file.write_text(
                generated_code,
                encoding="utf-8"
            )

            print("Generation successful!")
            print(f"Saved to: {output_file}")

        except Exception as error:
            print("Generation failed!")
            print(type(error).__name__)
            print(str(error)[:500])


if __name__ == "__main__":
    run_generation_tests()
