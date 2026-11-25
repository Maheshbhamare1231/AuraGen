
from pathlib import Path


# Locate the design system file
DESIGN_SYSTEM_PATH = Path(__file__).parent / "design_system.md"


def load_design_system():
    """Read AuraGen's UI design rules."""

    if not DESIGN_SYSTEM_PATH.exists():
        raise FileNotFoundError("design_system.md not found")

    return DESIGN_SYSTEM_PATH.read_text(encoding="utf-8")


def get_cognitive_load_level(score):
    """Convert cognitive load score into a level."""

    if score is None:
        return "Not provided"

    if score < 40:
        return "Low"

    elif score < 70:
        return "Medium"

    return "High"


def build_ui_prompt(
    user_request,
    form_context="",
    cognitive_load_score=None
):
    """Build a cognitive-load-aware AuraGen prompt."""

    design_system = load_design_system()

    load_level = get_cognitive_load_level(
        cognitive_load_score
    )

    if cognitive_load_score is None:

        simplification_instruction = """
No cognitive load score was provided.
Follow the user's request and maintain a simple,
accessible interface.
"""

    elif load_level == "Low":

        simplification_instruction = """
COGNITIVE LOAD LEVEL: LOW

The interface has relatively low cognitive complexity.

Instructions:
1. Preserve the existing form structure where appropriate.
2. Make minor usability improvements.
3. Keep labels and instructions clear.
4. Avoid unnecessary redesign.
"""

    elif load_level == "Medium":

        simplification_instruction = """
COGNITIVE LOAD LEVEL: MEDIUM

The interface has moderate cognitive complexity.

Instructions:
1. Organize related fields into logical groups.
2. Improve spacing and visual hierarchy.
3. Remove unnecessary visual distractions.
4. Use clear and concise instructions.
5. Consider grouping fields into manageable steps.
"""

    else:

        simplification_instruction = """
COGNITIVE LOAD LEVEL: HIGH

The interface has high cognitive complexity.

Instructions:
1. Strongly simplify the user interface.
2. Divide long forms into smaller manageable steps.
3. Show only the most relevant fields at each step.
4. Group related fields logically.
5. Remove unnecessary visual distractions.
6. Use simple labels and short instructions.
7. Provide clear navigation between steps.
8. Preserve all essential form functionality and data.
9. Do not remove required information just to reduce complexity.
"""

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

COGNITIVE LOAD SCORE:
{cognitive_load_score}

COGNITIVE LOAD LEVEL:
{load_level}

COGNITIVE LOAD INSTRUCTIONS:
{simplification_instruction}

Generate the React component now.
"""

    return prompt


if __name__ == "__main__":

    test_prompt = build_ui_prompt(
        user_request="Simplify the financial form.",
        form_context=(
            "The form contains name, email, "
            "monthly income and other details."
        ),
        cognitive_load_score=85
    )

    print("AuraGen Cognitive Load Prompt Test")
    print("----------------------------------")
    print(test_prompt)

def build_repair_prompt(
    invalid_code,
    validation_error,
    user_request="",
    form_context="",
    cognitive_load_score=None
):
    """
    Build a prompt to repair invalid React JSX code.
    """

    design_system = load_design_system()

    load_level = get_cognitive_load_level(
        cognitive_load_score
    )

    return f"""
You are AuraGen, an expert React and JSX debugging assistant.

The previously generated React component contains a syntax error.

YOUR TASK:
Repair the provided React component.

IMPORTANT RULES:
1. Fix the reported JSX or JavaScript syntax error.
2. Preserve the original component's purpose and functionality.
3. Follow the AuraGen design system.
4. Use functional React components.
5. Use Tailwind CSS for styling.
6. Preserve cognitive-load simplification requirements.
7. Do not remove essential form fields or functionality.
8. Return only complete, corrected React component code.
9. Do not include Markdown code fences or explanations.
10. Ensure all JSX tags, brackets and parentheses are correctly closed.

AURAGEN DESIGN SYSTEM:
{design_system}

ORIGINAL USER REQUEST:
{user_request}

FORM CONTEXT:
{form_context}

COGNITIVE LOAD SCORE:
{cognitive_load_score}

COGNITIVE LOAD LEVEL:
{load_level}

BABEL VALIDATION ERROR:
{validation_error}

INVALID REACT CODE:
{invalid_code}

Return the complete corrected React component now.
"""
