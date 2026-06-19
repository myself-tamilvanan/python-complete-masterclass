# Chapter 39: PyTest Basics

## Source
Based on: 12 Hours Python Masterclass in Tamil by Data Engineering (Gowtham)
Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 08:53:56

## Overview
PyTest is the most popular Python testing framework. It makes writing and running tests simple, with powerful features like fixtures, parametrize, and plugins.

## Installation
```bash
pip install pytest
pip install pytest-cov   # Coverage reporting
```

## Running Tests
```bash
pytest                      # Run all tests
pytest test_file.py         # Run specific file
pytest -v                   # Verbose output
pytest -k "test_add"        # Run tests matching name
pytest --cov=mymodule       # With coverage
```

## Key Concepts
- **Test function**: Any function starting with test_
- **Assertion**: assert statement for checking results
- **Fixture**: Reusable setup/teardown with @pytest.fixture
- **Parametrize**: Run same test with multiple inputs
- **Conftest.py**: Shared fixtures across test files

## Test File Structure
```
test_file.py   (or file_test.py)
def test_feature():
    # Arrange
    # Act
    # Assert
```

## Learning Outcomes
- Write test functions with pytest
- Use fixtures for setup and teardown
- Parametrize tests for multiple inputs
- Test exceptions with pytest.raises
- Generate coverage reports