# Chapter 46: PIP & PyPI Explained

## Source
Based on: 12 Hours Python Masterclass in Tamil by Data Engineering (Gowtham)
Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 10:50:10

## Overview
PIP is Python package installer. PyPI (Python Package Index) is the central repository at pypi.org. Together they are how Python developers share and install code.

## Essential PIP Commands
| Command                               | Purpose                     |
|---------------------------------------|-----------------------------|
| pip install package                   | Install package             |
| pip install package==1.2.3            | Specific version            |
| pip install -r requirements.txt       | Install from file           |
| pip uninstall package                 | Remove package              |
| pip list                              | List installed packages     |
| pip show package                      | Package details             |
| pip freeze > requirements.txt         | Export installed packages   |
| pip install --upgrade package         | Upgrade package             |

## Virtual Environments (Best Practice)
```bash
python3 -m venv myenv              # Create
source myenv/bin/activate          # Activate (Mac/Linux)
myenv\Scripts\activate            # Activate (Windows)
deactivate                         # Exit venv
```

## Semantic Versioning (MAJOR.MINOR.PATCH)
- MAJOR: Breaking changes
- MINOR: New features (backward compatible)
- PATCH: Bug fixes

## Learning Outcomes
- Install and manage Python packages with PIP
- Create and use virtual environments
- Generate and use requirements.txt
- Understand package versioning