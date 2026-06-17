# Chapter 53: Logging
# Python Complete Masterclass
# Source: freeCodeCamp Intermediate Python by Patrick Loeber
# ============================================

import logging

# -----------------------------------------------
# SECTION 1: Basic Logging
# -----------------------------------------------

print("--- Basic Logging ---")

# Default level is WARNING - only WARNING and above show
logging.warning("This is a warning")
logging.error("This is an error")
logging.critical("This is critical")

# These do NOT show by default (below WARNING):
logging.debug("This is debug - hidden by default")
logging.info("This is info - hidden by default")

# -----------------------------------------------
# SECTION 2: Configuration with basicConfig
# -----------------------------------------------

print("\n--- basicConfig ---")

# Reset root logger handlers
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# Configure logging level and format
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logging.debug("Debug message - now visible")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")

# -----------------------------------------------
# SECTION 3: Logging to a File
# -----------------------------------------------

print("\n--- Logging to File ---")

# Create a logger
file_logger = logging.getLogger("file_logger")
file_logger.setLevel(logging.DEBUG)

# Create file handler
fh = logging.FileHandler("app.log")
fh.setLevel(logging.DEBUG)

# Create formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)

# Add handler to logger
file_logger.addHandler(fh)

file_logger.debug("Logged to file: debug")
file_logger.info("Logged to file: info")
file_logger.warning("Logged to file: warning")

print("Check app.log for file output")

# -----------------------------------------------
# SECTION 4: Multiple Handlers
# -----------------------------------------------

print("\n--- Multiple Handlers ---")

# Logger with both console and file handlers
logger = logging.getLogger("multi_handler")
logger.setLevel(logging.DEBUG)

# Console handler - only show WARNING and above
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)
ch.setFormatter(logging.Formatter("CONSOLE: %(levelname)s - %(message)s"))

# File handler - record everything
fh2 = logging.FileHandler("debug.log")
fh2.setLevel(logging.DEBUG)
fh2.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

logger.addHandler(ch)
logger.addHandler(fh2)

logger.debug("Debug: goes to file only")
logger.info("Info: goes to file only")
logger.warning("Warning: goes to console AND file")
logger.error("Error: goes to console AND file")

# -----------------------------------------------
# SECTION 5: Logging in Practice
# -----------------------------------------------

print("\n--- Logging in Practice ---")

def divide(a, b):
    try:
        result = a / b
        logging.debug(f"divide({a}, {b}) = {result}")
        return result
    except ZeroDivisionError:
        logging.error(f"divide({a}, {b}): division by zero!")
        return None

divide(10, 2)
divide(10, 0)

# Clean up log files
import os
for log_file in ["app.log", "debug.log"]:
    if os.path.exists(log_file):
        os.remove(log_file)

print("\n" + "="*50)
print("Chapter 53 Complete!")
print("="*50)
