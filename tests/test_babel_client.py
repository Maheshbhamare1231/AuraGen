import unittest

from backend.babel_client import validate_jsx


class TestBabelClient(unittest.TestCase):

    def test_valid_jsx(self):
        code = """
        import React from 'react';

        function TestComponent() {
            return <div>Hello AuraGen</div>;
        }

        export default TestComponent;
        """

        result = validate_jsx(code)

        self.assertTrue(result["valid"])

    def test_invalid_jsx(self):
        code = """
        function TestComponent() {
            return <div>Hello AuraGen</span>;
        }
        """

        result = validate_jsx(code)

        self.assertFalse(result["valid"])


if __name__ == "__main__":
    unittest.main()