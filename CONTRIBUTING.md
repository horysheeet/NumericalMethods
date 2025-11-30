# Contributing to Numerical Methods Calculator

Thank you for considering contributing to the Numerical Methods Calculator! This document provides guidelines and instructions for contributing to this project.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
- [Code Style Guidelines](#code-style-guidelines)
- [Testing Requirements](#testing-requirements)
- [Pull Request Process](#pull-request-process)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)

## Code of Conduct

This project adheres to a code of conduct that all contributors are expected to follow:

- Be respectful and inclusive
- Welcome newcomers and help them get started
- Focus on constructive feedback
- Accept criticism gracefully
- Prioritize the community's best interests

## Getting Started

### Prerequisites

Before contributing, ensure you have:

- **Python 3.8+** installed
- **Git** for version control
- A **GitHub account**
- Basic knowledge of numerical methods (helpful but not required)

### Fork and Clone

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/NumericalMethods.git
   cd NumericalMethods
   ```
3. **Add upstream remote**:
   ```bash
   git remote add upstream https://github.com/horysheeet/NumericalMethods.git
   ```

## Development Setup

### 1. Create Virtual Environment

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install Dependencies

```bash
# Production dependencies
pip install -r requirements.txt

# Development dependencies
pip install -r requirements-dev.txt
```

### 3. Verify Installation

```bash
# Run tests to ensure everything works
pytest test_numerical_methods.py -v

# Start the server
python main.py
```

Visit `http://localhost:8000` to confirm the application is running.

## How to Contribute

### Types of Contributions

We welcome various types of contributions:

1. **Bug Fixes** - Fix issues in existing code
2. **New Features** - Add new numerical methods or functionality
3. **Documentation** - Improve README, docstrings, or comments
4. **Tests** - Add or improve test coverage
5. **Performance** - Optimize existing algorithms
6. **UI/UX** - Enhance templates and styling

### Contribution Workflow

1. **Check existing issues** to avoid duplicate work
2. **Create an issue** if one doesn't exist (for bugs or features)
3. **Get feedback** on your proposed changes
4. **Create a feature branch** from `main`
5. **Make your changes** with clear, focused commits
6. **Write/update tests** for your changes
7. **Run tests** to ensure everything passes
8. **Submit a pull request** with a clear description

## Code Style Guidelines

### Python Style (PEP 8)

We follow PEP 8 with some modifications:

- **Line length**: 100 characters (not 79)
- **Indentation**: 4 spaces (no tabs)
- **Naming conventions**:
  - Functions/variables: `snake_case`
  - Classes: `PascalCase`
  - Constants: `UPPER_CASE`

### Code Formatting

Use **Black** for automatic formatting:

```bash
# Format specific files
black main.py jacobi.py

# Format entire project
black .
```

### Linting

Use **flake8** to check for issues:

```bash
flake8 . --max-line-length=100 --exclude=.venv
```

### Type Hints

Add type hints to all function signatures:

```python
def jacobi_method(
    matrix_a: list[list[float]], 
    vector_b: list[float], 
    tolerance: float = 1e-6
) -> dict[str, any]:
    """
    Solve Ax = b using Jacobi iteration.
    
    Args:
        matrix_a: Coefficient matrix A
        vector_b: Right-hand side vector b
        tolerance: Convergence tolerance
        
    Returns:
        Dictionary containing solution, iterations, and error
    """
    pass
```

### Docstrings

Use Google-style docstrings:

```python
def calculate_derivative(func: str, x: float, h: float = 0.01) -> float:
    """
    Calculate the derivative of a function at a point.
    
    Args:
        func: Mathematical function as a string (e.g., "x**2")
        x: Point at which to evaluate derivative
        h: Step size for finite difference (default: 0.01)
        
    Returns:
        Approximate value of f'(x)
        
    Raises:
        ValueError: If step size h is too small or too large
        
    Example:
        >>> calculate_derivative("x**2", 2.0, 0.01)
        4.0001
    """
    pass
```

## Testing Requirements

### Writing Tests

All new features must include tests:

```python
import pytest
from jacobi import jacobi_method

def test_jacobi_simple_system():
    """Test Jacobi method on a simple 2x2 system."""
    A = [[4, -1], [-1, 4]]
    b = [5, 5]
    
    result = jacobi_method(A, b)
    
    assert result["success"] == True
    assert abs(result["solution"][0] - 1.666667) < 1e-5
    assert abs(result["solution"][1] - 1.666667) < 1e-5
```

### Running Tests

```bash
# Run all tests
pytest test_numerical_methods.py -v

# Run with coverage
pytest test_numerical_methods.py --cov=. --cov-report=html

# Run specific test
pytest test_numerical_methods.py::test_jacobi_simple_system -v
```

### Coverage Requirements

- **Minimum coverage**: 80% for new code
- **Target coverage**: 90%+
- View coverage report: `htmlcov/index.html`

## Pull Request Process

### Before Submitting

- [ ] Code follows style guidelines (run `black` and `flake8`)
- [ ] All tests pass (`pytest test_numerical_methods.py -v`)
- [ ] New tests added for new features
- [ ] Documentation updated (README, docstrings)
- [ ] CHANGELOG.md updated (if applicable)
- [ ] Commit messages are clear and descriptive

### PR Template

When creating a PR, include:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Code refactoring

## Testing
- [ ] All existing tests pass
- [ ] New tests added
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex logic
- [ ] Documentation updated
- [ ] No new warnings generated
```

### Review Process

1. **Automated checks** run on your PR (tests, linting)
2. **Maintainer review** - usually within 2-3 days
3. **Requested changes** - address feedback and push updates
4. **Approval and merge** - after all checks pass

## Reporting Bugs

### Bug Report Template

```markdown
**Describe the bug**
Clear description of the issue

**To Reproduce**
Steps to reproduce:
1. Go to '...'
2. Enter data '...'
3. Click on '...'
4. See error

**Expected behavior**
What you expected to happen

**Screenshots**
If applicable, add screenshots

**Environment**
- OS: [e.g., Windows 11]
- Python Version: [e.g., 3.11.0]
- Browser: [e.g., Chrome 120]

**Additional context**
Any other relevant information
```

### Where to Report

- **GitHub Issues**: https://github.com/horysheeet/NumericalMethods/issues
- Label the issue as `bug`

## Suggesting Enhancements

### Enhancement Request Template

```markdown
**Is your feature request related to a problem?**
Clear description of the problem

**Describe the solution you'd like**
What you want to happen

**Describe alternatives you've considered**
Alternative solutions or features

**Additional context**
Mockups, examples, or references
```

### Feature Discussion

- Open an issue with the `enhancement` label
- Wait for maintainer feedback before implementing
- Discuss implementation approach
- Get approval before starting work

## Development Tips

### Common Tasks

```bash
# Update dependencies
pip install -r requirements.txt --upgrade

# Check for security vulnerabilities
pip install safety
safety check

# Run in development mode
uvicorn main:app --reload --log-level debug

# Generate requirements.txt
pip freeze > requirements.txt
```

### Project Structure

```
numerical-methods-calculator/
├── main.py              # FastAPI application
├── jacobi.py            # Jacobi method implementation
├── regula_falsi.py      # Regula-Falsi implementation
├── forward_fd.py        # Forward finite difference
├── backward_fd.py       # Backward finite difference
├── center_fd.py         # Center finite difference
├── config.json          # Configuration
├── config_loader.py     # Config management
├── test_numerical_methods.py  # Tests
├── templates/           # HTML templates
└── static/             # CSS files
```

### Adding a New Numerical Method

1. Create new module (e.g., `newton_raphson.py`)
2. Implement the algorithm with proper error handling
3. Add configuration to `config.json`
4. Create HTML template in `templates/`
5. Add routes in `main.py` (GET and POST)
6. Add API endpoint
7. Write comprehensive tests
8. Update README.md documentation

## Questions?

If you have questions, feel free to:

- Open a GitHub Discussion
- Comment on existing issues
- Contact the maintainers

## Recognition

Contributors will be recognized in:

- GitHub contributors list
- CHANGELOG.md for significant contributions
- README.md acknowledgments section

---

**Thank you for contributing to Numerical Methods Calculator!** 🎉

Your contributions help make this project better for everyone.
