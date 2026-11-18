from pydantic import BaseModel, Field, field_validator
from typing import Optional


class UIComponentResponse(BaseModel):
    """
    Schema for AI-generated React UI components.
    """

    component_name: str = Field(
        description="Name of the generated React component"
    )

    code: str = Field(
        min_length=1,
        description="Complete React JSX component code"
    )

    explanation: Optional[str] = Field(
        default=None,
        description="Short explanation of the generated component"
    )

    language: str = Field(
        default="jsx",
        description="Programming language of the generated component"
    )

    @field_validator("component_name")
    @classmethod
    def validate_component_name(cls, value):
        if not value.strip():
            raise ValueError("Component name cannot be empty")

        return value.strip()

    @field_validator("code")
    @classmethod
    def validate_code(cls, value):
        if not value.strip():
            raise ValueError("Generated code cannot be empty")

        return value.strip()

    @field_validator("language")
    @classmethod
    def validate_language(cls, value):
        allowed_languages = ["jsx", "javascript"]

        if value.lower() not in allowed_languages:
            raise ValueError("Unsupported programming language")

        return value.lower()
    
import re


def extract_react_code(raw_output: str) -> str:
    """
    Extract React code from Gemini's response.
    Removes Markdown code fences if present.
    """

    raw_output = raw_output.strip()

    # Remove Markdown code fences
    if raw_output.startswith("```"):
        lines = raw_output.splitlines()

        if lines[-1].strip() == "```":
            lines = lines[:-1]

        lines = lines[1:]
        raw_output = "\n".join(lines)

    return raw_output.strip()


def validate_generated_ui(raw_output: str) -> UIComponentResponse:
    """
    Extract and validate AI-generated React UI code.
    """

    code = extract_react_code(raw_output)

    # Detect React component name
    match = re.search(
        r"(?:function|const|class)\s+([A-Z][A-Za-z0-9_]*)",
        code
    )

    if match:
        component_name = match.group(1)
    else:
        component_name = "GeneratedComponent"

    # Validate using Pydantic
    response = UIComponentResponse(
        component_name=component_name,
        code=code,
        explanation="AI-generated React component",
        language="jsx"
    )

    return response

