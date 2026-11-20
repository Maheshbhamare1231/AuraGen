# AuraGen

### Self-Healing Generative UI via Cognitive Load

AuraGen aims to simplify complex user interfaces based on cognitive friction and user interaction.

## My Contribution

Member 1 - AI & Backend Developer

## Day 1 Progress

- Python environment configured.
- Virtual environment created.
- Required Python packages installed.
- Backend project structure created.
- Environment verification completed.

## Day 2 Progress

- Integrated Google Gemini with LangChain.
- Configured API key using environment variables.
- Successfully tested Gemini API connection.
- Generated the first React functional component.
- Tested React JSX generation with Tailwind CSS.
- Saved FinancialForm.jsx in generated_components.

## Day 3 Progress

- Created ai_engine/design_system.md.
- Defined AuraGen UI design guidelines.
- Documented colors, typography, spacing and component styling.
- Added React component development guidelines.
- Defined accessibility requirements.
- Established guidelines for simplifying complex forms while maintaining design consistency.

## Day 4 Progress

- Created ai_engine/prompts.py.
- Implemented dynamic design-system loading.
- Developed the AuraGen system prompt.
- Integrated the prompt builder with Gemini.
- Updated ai_engine/llm.py.
- Implemented React component generation using user requests and form context.
- Successfully generated a multi-step financial form.

## Day 5 Progress

- Created automated UI generation test script.
- Tested generation of multiple React components.
- Generated FinancialWizard.jsx.
- Generated RegistrationForm.jsx.
- Generated ContactForm.jsx.
- Tested design-system consistency across generated components.
- Saved generated components in generated_components/.

## AI Model

Gemini 3.5 Flash-Lite

## Technologies

- Python
- LangChain
- LangChain Google GenAI
- FastAPI
- Pydantic
- Python-dotenv
- React
- Tailwind CSS

## Project Structure

- backend/
- ai_engine/
- validator/
- tests/
- generated_components/

## Setup

Install dependencies:

pip install -r requirements.txt

Run environment check:

python day1_check.py

## Current Status

Day 1 - Environment setup completed.

Day 2 - Gemini integration and first React component generation completed.

Day 3 - Design system development completed.

Day 4 - AI prompt engineering and Gemini-powered UI generation completed.

Day 5 - Multiple React component generation and testing completed.

## Day 6 – Structured Output Validation

Implemented Pydantic-based validation for AI-generated React UI components.

### Features
- Defined UIComponentResponse schema.
- Validated component name.
- Validated generated code.
- Validated supported programming languages.
- Extracted React code from Markdown code blocks.
- Integrated validation with Gemini UI generation.
- Tested valid and invalid responses.
- Tested actual Gemini-generated React components.

### Validation Pipeline

User Request → Gemini → React Code Extraction → Pydantic Validation → Validated UI Response

### Files Created/Updated
- backend/schemas.py
- tests/test_validation.py
- tests/test_ai_validation.py
- ai_engine/llm.py


## Day 7 – FastAPI Backend Integration

### Objective
Created a FastAPI backend to expose AuraGen's AI-powered UI generation and validation functionality through REST API endpoints.

### Implemented Features
- `GET /` – Checks whether the AuraGen API is running.
- `GET /health` – Checks backend health.
- `POST /generate-ui` – Accepts a UI simplification request, generates React JSX using Gemini, validates the response using Pydantic, and returns JSON.
- Request validation using Pydantic.
- Invalid requests are rejected with HTTP 422 before calling Gemini.
- API documentation and testing through Swagger UI.

### Sample API Request
```json
{
  "user_request": "Simplify the financial form into two steps with a clean modern design.",
  "form_context": "The existing form contains full name, email address and monthly income."
}
```

### Testing Results
- `GET /` – HTTP 200
- `GET /health` – HTTP 200
- `POST /generate-ui` with a valid request – HTTP 200
- `POST /generate-ui` with an invalid short request – HTTP 422

### Day 7 Outcome
Successfully connected the Gemini generation and Pydantic validation pipeline to FastAPI. The backend can now receive requests through an API and return validated React component code.


## Day 8 – Babel JSX Validation Integration

### Objective
Integrated Node.js and Babel with the Python FastAPI backend to validate AI-generated React JSX syntax.

### Technologies Used
- Node.js
- npm
- @babel/parser
- Python
- FastAPI

### Implementation
1. Created a separate `babel-validator` Node.js project.
2. Installed the `@babel/parser` package.
3. Created `validator.js` to parse and validate React JSX.
4. Created `backend/babel_client.py` to communicate with Node.js using Python subprocess.
5. Integrated Babel validation into the `/generate-ui` FastAPI endpoint.

### Testing Results
- Valid JSX was successfully accepted.
- Invalid JSX was successfully rejected.
- Python-to-Node.js communication was tested.
- FastAPI successfully returned generated JSX with Babel validation results.

### Example Validation Response

```json
{
  "valid": true,
  "message": "React JSX syntax is valid."
}
```

### Day 8 Outcome
Successfully integrated Babel syntax validation into the AuraGen AI generation pipeline.
