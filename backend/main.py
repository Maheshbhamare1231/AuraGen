
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from ai_engine.llm import generate_validated_ui
from backend.babel_client import validate_jsx


# Create FastAPI application
app = FastAPI(
    title="AuraGen API",
    description="AI-powered self-healing generative UI backend",
    version="1.0.0"
)


# Request schema
class GenerateUIRequest(BaseModel):

    user_request: str = Field(
        min_length=5,
        description="Description of the UI modification"
    )

    form_context: str = Field(
        default="",
        description="Existing form information or context"
    )


# Root endpoint
@app.get("/")
def home():

    return {
        "message": "AuraGen API is running!",
        "status": "success"
    }


# Health check endpoint
@app.get("/health")
def health_check():

    return {
        "status": "healthy",
        "service": "AuraGen Backend"
    }


# UI generation endpoint
@app.post("/generate-ui")
def generate_ui_endpoint(request: GenerateUIRequest):

    try:

        # Step 1: Generate React component using Gemini
        result = generate_validated_ui(
            user_request=request.user_request,
            form_context=request.form_context
        )

        # Step 2: Validate generated JSX using Babel
        babel_result = validate_jsx(result.code)

        # Step 3: Return generation and validation results
        return {
            "status": (
                "success" if babel_result["valid"]
                else "validation_failed"
            ),

            "component_name": result.component_name,

            "language": result.language,

            "code": result.code,

            "explanation": result.explanation,

            "babel_validation": babel_result
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"UI generation failed: {str(error)}"
        )
