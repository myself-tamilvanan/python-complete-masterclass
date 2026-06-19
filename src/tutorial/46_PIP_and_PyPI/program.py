# Chapter 46: PIP & PyPI Explained
# 12 Hours Python Masterclass in Tamil - Data Engineering (Gowtham)
# Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 10:50:10
# ============================================

import json
import os
import subprocess
import sys

print("--- PIP & PyPI ---")

print("Python version:", sys.version.split()[0])
print("Python executable:", sys.executable)

# Get PIP version
try:
    result = subprocess.run(
        [sys.executable, "-m", "pip", "--version"], capture_output=True, text=True
    )
    print("PIP version:", result.stdout.strip())
except Exception as e:
    print("PIP check failed:", e)

# List installed packages
try:
    result = subprocess.run(
        [sys.executable, "-m", "pip", "list", "--format=json"], capture_output=True, text=True
    )
    packages = json.loads(result.stdout)
    print(f"\nTotal packages installed: {len(packages)}")
    print("First 10:")
    for pkg in packages[:10]:
        print(f"  {pkg['name']:<30} {pkg['version']}")
except Exception as e:
    print("Error:", e)

# Create requirements.txt
requirements = [
    "flask==2.3.3",
    "pandas>=1.5.0",
    "numpy>=1.23.0",
    "requests>=2.31.0",
    "pytest>=7.4.0",
]

with open("requirements_example.txt", "w") as f:
    f.write("\n".join(requirements))
print("\nrequirements_example.txt created")

print("\n--- PIP Commands Reference ---")
commands = [
    ("Install", "pip install flask"),
    ("Specific version", "pip install flask==2.3.0"),
    ("From file", "pip install -r requirements.txt"),
    ("Uninstall", "pip uninstall flask"),
    ("List all", "pip list"),
    ("Show info", "pip show flask"),
    ("Freeze", "pip freeze > requirements.txt"),
    ("Upgrade", "pip install --upgrade flask"),
]
for action, cmd in commands:
    print(f"  {action:<20}: {cmd}")

print("\n--- Virtual Environment Commands ---")
venv_cmds = [
    ("Create", "python3 -m venv myenv"),
    ("Activate Mac/Linux", "source myenv/bin/activate"),
    ("Activate Windows", "myenv\\Scripts\\activate"),
    ("Deactivate", "deactivate"),
    ("Delete", "rm -rf myenv"),
]
for action, cmd in venv_cmds:
    print(f"  {action:<25}: {cmd}")

os.remove("requirements_example.txt")

print("\n" + "=" * 50)
print("Chapter 46 Complete!")
print("=" * 50)
