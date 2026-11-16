
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found in .env")

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    api_key=api_key,
    timeout=120,
    max_retries=0
)
def test_connection():
    print("Connecting to Gemini...")

    try:
        response = llm.invoke(
            "Reply with exactly: AuraGen Gemini connection successful!"
        )
        print("\nGemini response:")
        print(response.content)

    except Exception as error:
        print("\nConnection failed:")
        print(type(error).__name__)
        print(str(error)[:1000])


if __name__ == "__main__":
    response = llm.invoke("""
Generate a simple React functional component named FinancialForm.

Requirements:
1. Include Name, Email and Monthly Income fields.
2. Include a Submit button.
3. Use standard React JSX.
4. Use Tailwind CSS classes.
5. Return only the React component code.
""")

print("\nGenerated React Component:\n")

for block in response.content:
    if isinstance(block, dict) and block.get("type") == "text":
        print(block.get("text", ""))
    elif isinstance(block, str):
        print(block)
