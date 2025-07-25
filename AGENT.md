# Agent Instructions

The purpose of this file is to provide basic guidelines for working with the repository.

## General Guidelines
- Follow [PEP 8](https://peps.python.org/pep-0008/) style conventions for all Python code.
- Prefer clear variable names and include docstrings for functions.
- Keep lines under 79 characters where practical.

## Formatting
- Format Python files using [Black](https://github.com/psf/black) before committing. The default settings are sufficient.

## Validation
- After modifying any Python file, run `python -m py_compile <file>` to check for syntax errors.
- If a `tests` directory is present, run `pytest` and ensure all tests pass before committing.

## Commit Messages
- Use descriptive commit messages that summarise the change.
- Avoid large unrelated changes in a single commit.

