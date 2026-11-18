from backend.schemas import UIComponentResponse, validate_generated_ui


def test_valid_response():
    response = UIComponentResponse(
        component_name="FinancialWizard",
        code="function FinancialWizard() { return <div>Hello</div>; }",
        explanation="A simplified financial form",
        language="jsx"
    )

    print("Valid response:")
    print(response.model_dump())


def test_invalid_empty_code():
    try:
        UIComponentResponse(
            component_name="FinancialWizard",
            code="",
            language="jsx"
        )

    except ValueError as error:
        print("\nInvalid response correctly rejected:")
        print(error)


def test_invalid_language():
    try:
        UIComponentResponse(
            component_name="FinancialWizard",
            code="function FinancialWizard() {}",
            language="python"
        )

    except ValueError as error:
        print("\nInvalid language correctly rejected:")
        print(error)


def test_ai_output_validation():

    sample_ai_output = """
```jsx
function FinancialWizard() {
    return (
        <div>
            <h1>Financial Information</h1>
        </div>
    );
}

export default FinancialWizard;

```
    """
    
    response = validate_generated_ui(sample_ai_output)

    print("\nAI output validation:")
    print("Component Name:", response.component_name)
    print("Language:", response.language)
    print("Validated Code:")
    print(response.code)


if __name__ == "__main__":
    test_valid_response()
    test_invalid_empty_code()
    test_invalid_language()
    test_ai_output_validation()