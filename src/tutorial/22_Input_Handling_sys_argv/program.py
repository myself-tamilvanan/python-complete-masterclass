# Chapter 22: Input Handling with sys.argv
# 12 Hours Python Masterclass in Tamil - Data Engineering (Gowtham)
# Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 02:28:28
# ============================================

import argparse
import os
import sys

# -----------------------------------------------
# SECTION 1: sys.argv Basics
# -----------------------------------------------

print("--- sys.argv ---")

# sys.argv[0] is always the script name
print("Script name:", sys.argv[0])
print("All arguments:", sys.argv)
print("Number of args:", len(sys.argv))

# Typical usage pattern
if len(sys.argv) > 1:
    name = sys.argv[1]
    print(f"Hello, {name}!")
else:
    print("Usage: python3 program.py <your_name>")
    print("Running with defaults...")
    name = "World"
    print(f"Hello, {name}!")

# -----------------------------------------------
# SECTION 2: Parsing sys.argv Manually
# -----------------------------------------------

print("\n--- Manual Argument Parsing ---")


def parse_args_manually():
    """Parse command-line args manually from sys.argv."""
    args = {"name": "default_user", "age": 25, "verbose": False}

    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg == "--name" and i + 1 < len(sys.argv):
            args["name"] = sys.argv[i + 1]
            i += 2
        elif arg == "--age" and i + 1 < len(sys.argv):
            args["age"] = int(sys.argv[i + 1])
            i += 2
        elif arg == "--verbose":
            args["verbose"] = True
            i += 1
        else:
            i += 1
    return args


parsed = parse_args_manually()
print("Parsed args:", parsed)

# -----------------------------------------------
# SECTION 3: argparse (Professional CLI)
# -----------------------------------------------

print("\n--- argparse ---")


# argparse is the recommended way to build CLI tools
def create_parser():
    parser = argparse.ArgumentParser(
        description="A sample CLI tool", epilog="Example: python3 program.py --name Alice --age 30"
    )

    # Positional argument (required)
    # parser.add_argument("filename", help="Input file to process")

    # Optional argument
    parser.add_argument("--name", "-n", default="World", help="Your name (default: World)")

    # Optional with type conversion
    parser.add_argument(
        "--count", "-c", type=int, default=1, help="Number of repetitions (default: 1)"
    )

    # Boolean flag
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output")

    # Choice constraint
    parser.add_argument(
        "--format", choices=["json", "csv", "txt"], default="txt", help="Output format"
    )
    return parser


parser = create_parser()
# Parse only known args (so script works standalone without the actual args)
args, _ = parser.parse_known_args([])

print(f"Name: {args.name}")
print(f"Count: {args.count}")
print(f"Verbose: {args.verbose}")
print(f"Format: {args.format}")

# -----------------------------------------------
# SECTION 4: Environment Variables
# -----------------------------------------------

print("\n--- Environment Variables ---")

# Read environment variable (secure way to pass secrets)
db_password = os.environ.get("DB_PASSWORD", "default_password")
api_key = os.environ.get("API_KEY", "not_set")

print(f"DB_PASSWORD: {db_password}")
print(f"API_KEY: {api_key}")

# Set environment variable in Python (for subprocess)
os.environ["MY_APP_ENV"] = "development"
print(f"MY_APP_ENV: {os.environ.get('MY_APP_ENV')}")

# -----------------------------------------------
# SECTION 5: Interactive Input with Validation
# -----------------------------------------------

print("\n--- Interactive Input Validation ---")


def get_integer_input(prompt, min_val=None, max_val=None):
    """Get and validate integer input."""
    # For demonstration, use a fixed value instead of real input
    value_str = "25"  # Simulated user input
    print(f"{prompt} [simulated: {value_str}]")
    try:
        value = int(value_str)
        if min_val is not None and value < min_val:
            print(f"Must be at least {min_val}")
            return None
        if max_val is not None and value > max_val:
            print(f"Must be at most {max_val}")
            return None
        return value
    except ValueError:
        print("Invalid integer!")
        return None


age = get_integer_input("Enter your age:", min_val=0, max_val=150)
print(f"Accepted age: {age}")

print("\n" + "=" * 50)
print("Chapter 22 Complete!")
print("=" * 50)
