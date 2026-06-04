#!/usr/bin/env python3
import sys
import json

def main():
    try:
        # Read the tool execution parameters from stdin
        input_data = json.load(sys.stdin)
    except json.JSONDecodeError:
        # If no valid JSON is provided, we can either allow or block.
        # For safety, we'll log a warning and allow.
        print("Warning: Could not parse stdin as JSON", file=sys.stderr)
        input_data = {}

    # Dump the input to stderr for debugging (this won't break the JSON output rule)
    print(f"Received tool input: {json.dumps(input_data)}", file=sys.stderr)

    # Check for dangerous patterns in the tool arguments
    # The input structure depends on the tool, but usually arguments are in "args" or "arguments"
    args_str = json.dumps(input_data.get("args", {}))

    forbidden_patterns = ["rm -rf /", "/etc/shadow", "DROP TABLE"]
    for pattern in forbidden_patterns:
        if pattern in args_str:
            print(f"Security Policy Violation: Detected forbidden pattern '{pattern}'", file=sys.stderr)
            sys.exit(2)  # Exit code 2 indicates a System Block

    # If everything is safe, output an empty JSON object (or valid response) and exit 0
    print("{}")
    sys.exit(0)

if __name__ == "__main__":
    main()
