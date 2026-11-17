
from pathlib import Path

# Locate the design system file
DESIGN_SYSTEM_PATH = Path(__file__).parent / "design_system.md"


def load_design_system():
    """Read AuraGen's UI design rules."""
    if not DESIGN_SYSTEM_PATH.exists():
        raise FileNotFoundError("design_system.md not found")

    return DESIGN_SYSTEM_PATH.read_text(encoding="utf-8")


def build_ui_prompt(user_request, form_context=""):
    """Build a prompt for generating AuraGen React components."""

    design_system = load_design_system()

    prompt = f"""
You are AuraGen, an expert React UI generation assistant.

Your task is to generate a simplified and user-friendly React component.

FOLLOW THESE RULES:

1. Follow the provided AuraGen design system.
2. Generate valid React JSX.
3. Use functional React components.
4. Use Tailwind CSS for styling.
5. Keep the interface simple and accessible.
6. Use clear labels and helpful instructions.
7. Do not remove important form functionality.
8. Use proper React state and event handling.
9. Do not generate unnecessary explanations.
10. Return only the React component code.

AURAGEN DESIGN SYSTEM:
{design_system}

USER REQUEST:
{user_request}

FORM CONTEXT:
{form_context}

Generate the React component now.
"""

    return prompt


if __name__ == "__main__":
    test_prompt = build_ui_prompt(
        user_request="Simplify the financial form into smaller steps.",
        form_context="The form contains name, email and monthly income."
    )

    print("AuraGen Prompt System Test")
    print("--------------------------")
    print(test_prompt)
