
from backend.babel_client import validate_jsx_with_babel


# Test 1: Valid JSX
valid_code = """
import React from 'react';

export default function App() {
    return <div>Hello AuraGen</div>;
}
"""

# Test 2: Invalid JSX
invalid_code = """
export default function App() {
    return <div>Hello AuraGen</div;
}
"""


print("Testing valid JSX...")
valid_result = validate_jsx_with_babel(valid_code)
print(valid_result)

print("\nTesting invalid JSX...")
invalid_result = validate_jsx_with_babel(invalid_code)
print(invalid_result)


# Verify expected results
assert valid_result["valid"] is True
assert invalid_result["valid"] is False

print("\nAll Babel integration tests passed!")
