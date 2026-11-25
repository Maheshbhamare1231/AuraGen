
import unittest
from unittest.mock import patch, MagicMock

from ai_engine.llm import generate_self_healing_ui


INVALID_JSX = """
function TestForm() {
    return <div><h1>Hello</div>;
}
"""

VALID_JSX = """
function TestForm() {
    return (
        <div>
            <h1>Hello</h1>
        </div>
    );
}
"""


class TestSelfHealing(unittest.TestCase):

    @patch("ai_engine.llm.llm")
    @patch("backend.babel_client.validate_jsx")
    @patch("ai_engine.llm.generate_ui")
    def test_invalid_jsx_is_repaired(
        self,
        mock_generate,
        mock_babel,
        mock_llm
    ):

        # Initial Gemini response
        mock_generate.return_value = INVALID_JSX

        # First Babel check fails; second succeeds
        mock_babel.side_effect = [
            {
                "valid": False,
                "message": "Expected closing JSX tag",
                "line": 2,
                "column": 35
            },
            {
                "valid": True,
                "message": "React JSX syntax is valid."
            }
        ]

        # Simulate Gemini's corrected response
        mock_response = MagicMock()
        mock_response.content = VALID_JSX
        mock_llm.invoke.return_value = mock_response

        result = generate_self_healing_ui(
            user_request="Create a simple form."
        )

        self.assertTrue(result["babel_validation"]["valid"])
        self.assertTrue(result["self_healed"])
        self.assertEqual(result["repair_attempts"], 1)
        self.assertEqual(result["component_name"], "TestForm")

        print("\nSelf-healing test passed!")
        print("Repair attempts:", result["repair_attempts"])

    @patch("backend.babel_client.validate_jsx")
    @patch("ai_engine.llm.generate_ui")
    def test_valid_jsx_needs_no_repair(
        self,
        mock_generate,
        mock_babel
    ):

        mock_generate.return_value = VALID_JSX

        mock_babel.return_value = {
            "valid": True,
            "message": "React JSX syntax is valid."
        }

        result = generate_self_healing_ui(
            user_request="Create a simple form."
        )

        self.assertTrue(result["babel_validation"]["valid"])
        self.assertFalse(result["self_healed"])
        self.assertEqual(result["repair_attempts"], 0)

        print("\nNo-repair test passed!")

    @patch("ai_engine.llm.llm")
    @patch("backend.babel_client.validate_jsx")
    @patch("ai_engine.llm.generate_ui")
    def test_repair_stops_after_max_attempts(
        self,
        mock_generate,
        mock_babel,
        mock_llm
    ):
        mock_generate.return_value = INVALID_JSX

        mock_babel.return_value = {
            "valid": False,
            "message": "Expected closing JSX tag",
            "line": 2,
            "column": 35
        }

        mock_response = MagicMock()
        mock_response.content = INVALID_JSX
        mock_llm.invoke.return_value = mock_response

        result = generate_self_healing_ui(
            user_request="Create a simple form.",
            max_repair_attempts=2
        )

        self.assertFalse(result["babel_validation"]["valid"])
        self.assertFalse(result["self_healed"])
        self.assertEqual(result["repair_attempts"], 2)
        self.assertEqual(mock_babel.call_count, 3)
        self.assertEqual(mock_llm.invoke.call_count, 2)

        print("\nMaximum repair limit test passed!")
if __name__ == "__main__":
    unittest.main()

    @patch("ai_engine.llm.llm")
    @patch("backend.babel_client.validate_jsx")
    @patch("ai_engine.llm.generate_ui")
    def test_repair_stops_after_max_attempts(
        self,
        mock_generate,
        mock_babel,
        mock_llm
    ):

        mock_generate.return_value = INVALID_JSX

        # All three Babel validations fail:
        # 1 initial validation + 2 repair validations
        mock_babel.return_value = {
            "valid": False,
            "message": "Expected closing JSX tag",
            "line": 2,
            "column": 35
        }

        mock_response = MagicMock()
        mock_response.content = INVALID_JSX
        mock_llm.invoke.return_value = mock_response

        result = generate_self_healing_ui(
            user_request="Create a simple form.",
            max_repair_attempts=2
        )

        self.assertFalse(result["babel_validation"]["valid"])
        self.assertFalse(result["self_healed"])
        self.assertEqual(result["repair_attempts"], 2)
        self.assertEqual(mock_babel.call_count, 3)
        self.assertEqual(mock_llm.invoke.call_count, 2)

        print("\nMaximum repair limit test passed!")
        print("Repair attempts:", result["repair_attempts"])
