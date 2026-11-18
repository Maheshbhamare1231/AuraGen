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