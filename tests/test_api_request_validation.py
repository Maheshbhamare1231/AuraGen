import unittest
from pydantic import ValidationError

from backend.main import GenerateUIRequest


class TestAPIRequestValidation(unittest.TestCase):

    def test_valid_request(self):
        request = GenerateUIRequest(
            user_request="Simplify my registration form",
            cognitive_load_score=85
        )
        self.assertEqual(request.cognitive_load_score, 85)

    def test_minimum_cognitive_score(self):
        request = GenerateUIRequest(
            user_request="Improve my registration form",
            cognitive_load_score=0
        )
        self.assertEqual(request.cognitive_load_score, 0)

    def test_maximum_cognitive_score(self):
        request = GenerateUIRequest(
            user_request="Improve my registration form",
            cognitive_load_score=100
        )
        self.assertEqual(request.cognitive_load_score, 100)

    def test_negative_cognitive_score(self):
        with self.assertRaises(ValidationError):
            GenerateUIRequest(
                user_request="Improve my registration form",
                cognitive_load_score=-1
            )

    def test_score_above_100(self):
        with self.assertRaises(ValidationError):
            GenerateUIRequest(
                user_request="Improve my registration form",
                cognitive_load_score=101
            )

    def test_short_user_request(self):
        with self.assertRaises(ValidationError):
            GenerateUIRequest(
                user_request="Hi",
                cognitive_load_score=50
            )

    def test_missing_score_is_allowed(self):
        request = GenerateUIRequest(
            user_request="Improve my registration form"
        )
        self.assertIsNone(request.cognitive_load_score)


if __name__ == "__main__":
    unittest.main()