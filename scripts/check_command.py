import json
import sys
import re


def main():
    payload = json.load(sys.stdin)

    tool_input = payload.get("tool_input", {})
    command = tool_input.get("command", "")

    if re.search(r"\brm\b", command):
        decision = {
            "decision": "deny",
            "reason": "Destructive rm commands are not allowed."
        }
    else:
        decision = {
            "decision": "allow",
            "reason": "Command passed the safety check."
        }

    print(json.dumps(decision))


if __name__ == "__main__":
    main()

