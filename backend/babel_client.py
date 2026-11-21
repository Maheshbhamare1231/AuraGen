
import json
import subprocess
from pathlib import Path


# Find AuraGen project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Locate Babel validator
VALIDATOR_PATH = (
    PROJECT_ROOT / "babel-validator" / "validator.js"
)


def validate_jsx(code: str) -> dict:
    """
    Send React JSX code to Node.js Babel validator.
    Return the validation result.
    """

    try:
        result = subprocess.run(
            ["node", str(VALIDATOR_PATH)],
            input=code,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=15,
            check=False
        )

        if not result.stdout.strip():
            return {
                "valid": False,
                "message": result.stderr.strip()
                or "Babel validator returned no output."
            }

        return json.loads(result.stdout)

    except subprocess.TimeoutExpired:
        return {
            "valid": False,
            "message": "Babel validation timed out."
        }

    except FileNotFoundError:
        return {
            "valid": False,
            "message": "Node.js or Babel validator file was not found."
        }

    except json.JSONDecodeError:
        return {
            "valid": False,
            "message": "Invalid response from Babel validator."
        }
