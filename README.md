# AuraGen

### Self-Healing Generative UI via Cognitive Load

AuraGen is a project that aims to simplify complex user interfaces based on cognitive friction and user interaction.

## My Contribution

**Member 1 – AI & Backend Developer**

## Day 1 – Environment Setup

- Python environment configured.
- Virtual environment created.
- Required Python packages installed.
- Backend project structure created.
- Environment verification completed.

## Day 2 – Gemini Integration

- Integrated Google Gemini with LangChain.
- Configured API key using environment variables.
- Successfully tested Gemini API connection.
- Generated the first React functional component.
- Tested React JSX generation with Tailwind CSS.
- Saved `FinancialForm.jsx` in `generated_components/`.

## Day 3 – Design System Development

- Created `ai_engine/design_system.md`.
- Defined AuraGen UI design guidelines.
- Documented colors, typography, spacing and component styling.
- Added React component development guidelines.
- Defined accessibility requirements.
- Established rules for simplifying complex forms while maintaining design consistency.

## Day 4 – AI Prompt Engineering and UI Generation

- Created `ai_engine/prompts.py`.
- Implemented dynamic design-system loading.
- Developed the AuraGen system prompt.
- Integrated the prompt builder with Gemini.
- Updated `ai_engine/llm.py`.
- Implemented React component generation using user requests and form context.
- Successfully generated a multi-step financial form using Gemini.

## AI Model

- Google Gemini 3.5 Flash-Lite

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

```text
AuraGen/
├── backend/
├── ai_engine/
│   ├── llm.py
│   ├── prompts.py
│   └── design_system.md
├── validator/
├── tests/
├── generated_components/
├── requirements.txt
└── README.md
```

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Run environment check:

```bash
python day1_check.py
```

## Current Progress

- Day 1 – Environment setup completed.
- Day 2 – Gemini integration and first React component generation completed.
- Day 3 – Design system development completed.
- Day 4 – AI prompt engineering and Gemini-powered UI generation completed.

## Project Goal

Build an AI-powered system that detects cognitive friction and dynamically simplifies complex React interfaces while maintaining design consistency and accessibility.
