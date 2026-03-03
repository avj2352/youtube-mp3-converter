import re
import sys

# conver filename to snake case format
def to_snake_case(text: str) -> str:
    """
    Convert any text string into snake_case format.

    Handles:
    - Spaces:           "Harry Potter"     -> "harry_potter"
    - CamelCase:        "HarryPotter"      -> "harry_potter"
    - Mixed delimiters: "harry-Potter_Fan" -> "harry_potter_fan"
    - Special chars:    "Hello, World!"    -> "hello_world"
    - Extra spaces:     "  Hello   World " -> "hello_world"
    - Acronyms:         "parseHTTPSRequest"-> "parse_https_request"
    - Numbers:          "Area51Secret"     -> "area51_secret"
    """

    # 1. Insert underscore between lowercase/digit and uppercase letter (camelCase)
    #    e.g., "HarryPotter" -> "Harry_Potter"
    text = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', text)

    # 2. Insert underscore between consecutive uppercase letters followed by lowercase
    #    e.g., "HTTPSRequest" -> "HTTPS_Request"
    text = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', text)

    # 3. Replace any non-alphanumeric characters (spaces, hyphens, dots, etc.) with underscore
    text = re.sub(r'[^a-zA-Z0-9]+', '_', text)

    # 4. Convert to lowercase
    text = text.lower()

    # 5. Strip leading/trailing underscores
    text = text.strip('_')

    return text


# ─── Demo ───────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # If a CLI argument is provided, convert it
    if len(sys.argv) > 1:
        input_text = " ".join(sys.argv[1:])
        print(to_snake_case(input_text))
    else:
        # Otherwise run built-in test cases
        test_cases = [
            "Harry Potter",
            "HarryPotter",
            "harry-potter",
            "harry.potter",
            "Harry  Potter  Fan",
            "  Hello, World!  ",
            "parseHTTPSRequest",
            "Area51Secret",
            "XMLParser",
            "myVariableName",
            "This is a TEST String",
            "__already__snake__",
            "MixedHYPHEN-and space_combined",
        ]

        print(f"{'Input':<35} => {'snake_case Output'}")
        print("-" * 60)
        for t in test_cases:
            print(f"{repr(t):<35} => {to_snake_case(t)}")

