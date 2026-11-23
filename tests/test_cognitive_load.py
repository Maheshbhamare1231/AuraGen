import unittest

from ai_engine.prompts import (
    get_cognitive_load_level,
    build_ui_prompt
)


class TestCognitiveLoad(unittest.TestCase):

    def test_low_load_level(self):
        self.assertEqual(get_cognitive_load_level(0), "Low")
        self.assertEqual(get_cognitive_load_level(25), "Low")
        self.assertEqual(get_cognitive_load_level(39), "Low")

    def test_medium_load_level(self):
        self.assertEqual(get_cognitive_load_level(40), "Medium")
        self.assertEqual(get_cognitive_load_level(55), "Medium")
        self.assertEqual(get_cognitive_load_level(69), "Medium")

    def test_high_load_level(self):
        self.assertEqual(get_cognitive_load_level(70), "High")
        self.assertEqual(get_cognitive_load_level(85), "High")
        self.assertEqual(get_cognitive_load_level(100), "High")

    def test_missing_score(self):
        self.assertEqual(
            get_cognitive_load_level(None),
            "Not provided"
        )

    def test_low_load_prompt(self):
        prompt = build_ui_prompt(
            user_request="Improve the registration form.",
            cognitive_load_score=25
        )
        self.assertIn("COGNITIVE LOAD LEVEL: LOW", prompt)

    def test_medium_load_prompt(self):
        prompt = build_ui_prompt(
            user_request="Organize the registration form.",
            cognitive_load_score=55
        )
        self.assertIn("COGNITIVE LOAD LEVEL: MEDIUM", prompt)

    def test_high_load_prompt(self):
        prompt = build_ui_prompt(
            user_request="Simplify the registration form.",
            cognitive_load_score=85
        )
        self.assertIn("COGNITIVE LOAD LEVEL: HIGH", prompt)

    def test_missing_score_prompt(self):
        prompt = build_ui_prompt(
            user_request="Improve the registration form."
        )
        self.assertIn("No cognitive load score was provided.", prompt)


if __name__ == "__main__":
    unittest.main()