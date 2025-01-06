import re
import sys
from pathlib import Path

REGEX_COMMIT_MESSAGE = "^[a-zA-Z]+-\d+: .{10,}\s*$"


def main():
    messageFile = sys.argv[1]

    if not Path(messageFile).exists():
        sys.exit(1)

    try:
        file = open(messageFile, "r")
        message = file.read()
    finally:
        file.close()

    if not re.match(REGEX_COMMIT_MESSAGE, message):
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    print("Run regex")
    main()
