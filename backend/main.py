
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from ai_engine.llm import generate_self_healing_ui
from ai_engine.prompts import get_cognitive_load_level


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

    cognitive_load_score: int | None = Field(
        default=None,
        ge=0,
        le=100,
        description="Cognitive load score between 0 and 100"
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
        # Step 1: Generate, validate, and repair React JSX
        result = generate_self_healing_ui(
            user_request=request.user_request,
            form_context=request.form_context,
            cognitive_load_score=request.cognitive_load_score
        )

        # Step 2: Get final Babel validation result
        babel_result = result["babel_validation"]

        # Step 3: Detect cognitive load level
        load_level = get_cognitive_load_level(
            request.cognitive_load_score
        )

        # Step 4: Return generation, validation, and repair results
        return {
            "status": (
                "success" if babel_result["valid"]
                else "validation_failed"
            ),
            "component_name": result["component_name"],
            "language": result["language"],
            "code": result["code"],
            "explanation": result["explanation"],
            "cognitive_load_score": request.cognitive_load_score,
            "cognitive_load_level": load_level,
            "babel_validation": babel_result,
            "self_healed": result["self_healed"],
            "repair_attempts": result["repair_attempts"]
        }

    except Exception as error:
        error_message = str(error)

        # Handle temporary Gemini service unavailability
        if "503" in error_message or "UNAVAILABLE" in error_message:
            raise HTTPException(
                status_code=503,
                detail=(
                    "Gemini AI is temporarily unavailable due to high demand. "
                    "Please try again after a short wait."
                )
            )

        # Handle other generation errors
        raise HTTPException(
            status_code=500,
            detail=f"UI generation failed: {error_message}"
        )
