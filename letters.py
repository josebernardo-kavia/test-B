"""Print a single random lowercase letter (a-z) to stdout when executed.

Uses only Python's standard library and produces no additional output beyond the letter.
"""

import random
import string


if __name__ == "__main__":
    print(random.choice(string.ascii_lowercase))
