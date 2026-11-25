
import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient
from backend.main import app


client = TestClient(app)


class TestAPISelfHealing(unittest.TestCase):

    @patch("backend.main.generate_self_healing_ui")
    def test_api_returns_self_healing_results(self, mock_generate):

        mock_generate.return_value = {
            "component_name": "RegistrationForm",
            "language": "jsx",
            "code": """
function RegistrationForm() {
    return <div><h1>Registration Form</h1></div>;
}
""",
            "explanation": "A simple registration form.",
            "babel_validation": {
                "valid": True,
                "message": "React JSX syntax is valid."
            },
            "self_healed": True,
            "repair_attempts": 1
        }

        response = client.post(
            "/generate-ui",
            json={
                "user_request": "Create a registration form.",
                "cognitive_load_score": 80
            }
        )

        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(data["status"], "success")
        self.assertEqual(data["component_name"], "RegistrationForm")
        self.assertTrue(data["babel_validation"]["valid"])
        self.assertTrue(data["self_healed"])
        self.assertEqual(data["repair_attempts"], 1)
        self.assertEqual(data["cognitive_load_level"], "High")

        mock_generate.assert_called_once()

        print("\nAPI self-healing integration test passed!")


if __name__ == "__main__":
    unittest.main()
