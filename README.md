# deep_learning_models

[![Lint & Format](https://github.com/DoronPor/deep_learning_models/actions/workflows/lint.yml/badge.svg)](https://github.com/DoronPor/deep_learning_models/actions/workflows/lint.yml)
[![Tests](https://github.com/DoronPor/deep_learning_models/actions/workflows/test.yml/badge.svg)](https://github.com/DoronPor/deep_learning_models/actions/workflows/test.yml)

Implementation of deep learning architectures via pytorch

## Code Quality

This project maintains high code quality standards through automated checks:

- **Code Formatting**: Uses [Black](https://github.com/psf/black) for consistent code style
- **Linting**: Uses [Ruff](https://github.com/astral-sh/ruff) for fast Python linting
- **Pre-commit Hooks**: Ensures all commits meet quality standards
  - Checks for common issues (trailing whitespace, merge conflicts, etc.)
  - Automatically formats code with Black
  - Runs Ruff for comprehensive linting

### Development Setup

1. Install pre-commit hooks:
```bash
pip install pre-commit
pre-commit install
```

2. Install development dependencies:
```bash
pip install black ruff pytest
```

### CI/CD Workflows

The project uses separate workflows for different concerns:
- **Lint & Format**: Checks code style and linting rules
- **Tests**: Runs the test suite

These checks run automatically on each commit and in GitHub Actions for all pull requests.