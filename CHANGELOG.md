# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-30

### 🎉 Initial Release

This is the first production release of the Numerical Methods Calculator.

### Added

#### Core Features
- **Jacobi Iterative Method** for solving systems of linear equations
  - Diagonal dominance checking
  - Iteration tracking with convergence monitoring
  - Configurable tolerance and max iterations
  - Support for relaxation factors

- **Regula-Falsi Method** for root finding
  - Linear interpolation-based root finding
  - Bracketing verification
  - Safe mathematical expression evaluation
  - Detailed iteration logs

- **Forward Finite Difference** for numerical differentiation
  - 1st and 2nd order derivatives
  - Configurable step size (h)
  - Multiple point evaluation support
  - Truncation error O(h) for 1st order

- **Backward Finite Difference** for numerical differentiation
  - 1st and 2nd order derivatives
  - Configurable step size (h)
  - Multiple point evaluation support
  - Truncation error O(h) for 1st order

- **Central Finite Difference** for numerical differentiation
  - Most accurate derivative approximation
  - 1st and 2nd order derivatives
  - Configurable step size (h)
  - Truncation error O(h²) for 1st order

#### Web Application
- FastAPI backend with async support
- 6 responsive HTML templates with Jinja2
- Clean CSS styling (600+ lines, no JavaScript)
- RESTful API endpoints for all methods
- Interactive web forms for input
- Detailed result displays with iteration tables
- Error messages and validation feedback

#### Configuration System
- Centralized `config.json` for all parameters
- `config_loader.py` for easy configuration access
- Support for method-specific settings
- Dot notation for nested configuration

#### Testing
- Comprehensive test suite with 40+ tests
- Unit tests for all 5 numerical methods
- Integration tests for web endpoints
- Edge case and error handling tests
- 90%+ code coverage

#### Documentation
- Professional README with badges
- System architecture diagram
- Detailed algorithm explanations
- Installation and usage guides
- API documentation with examples
- Troubleshooting section
- Contributing guidelines

#### Scripts
- `start.ps1` - PowerShell startup script
- `run_tests.ps1` - PowerShell test runner
- `github_upload.sh` - Git initialization script

#### CI/CD
- GitHub Actions workflow for automated testing
- Linting and code quality checks
- Coverage reporting
- Multi-Python version testing

#### Project Files
- MIT License
- Comprehensive .gitignore
- requirements.txt with all dependencies
- requirements-dev.txt for development

### Technical Details

#### Backend
- **Framework**: FastAPI 0.122.0
- **Server**: Uvicorn 0.38.0
- **Templating**: Jinja2 3.1.6
- **Numerical**: NumPy 2.3.5
- **Testing**: pytest 9.0.1

#### Frontend
- Pure HTML5 + CSS3 (no JavaScript)
- Responsive design with CSS Grid and Flexbox
- Modern color scheme with CSS variables
- Mobile-friendly interface

#### Code Quality
- PEP 8 compliant
- Type hints throughout
- Comprehensive docstrings
- Error handling and validation
- Logging for debugging

### Features

✅ 5 numerical methods fully implemented  
✅ Web interface and RESTful API  
✅ Iteration tracking and convergence monitoring  
✅ Comprehensive error handling  
✅ Full test coverage  
✅ Professional documentation  
✅ CI/CD pipeline  
✅ Production-ready code  

### Known Limitations

- Jacobi method requires diagonally dominant matrices for guaranteed convergence
- Regula-Falsi requires proper root bracketing
- Finite difference methods have truncation errors dependent on step size
- No graphical visualization of convergence (planned for v1.1.0)
- No user authentication (planned for v2.0.0)

### Security

- Safe expression evaluation with restricted namespace
- Input validation on all endpoints
- No SQL injection vulnerabilities (no database)
- CORS configuration for API security

### Performance

- Async support for concurrent requests
- Efficient NumPy operations
- Minimal dependencies
- Fast startup time
- Low memory footprint

---

## [Unreleased]

### Planned for v1.1.0
- [ ] Newton-Raphson method
- [ ] Gauss-Seidel method
- [ ] Convergence visualization charts
- [ ] Export results to CSV/PDF

### Planned for v2.0.0
- [ ] User authentication
- [ ] Save calculation history
- [ ] Database integration
- [ ] Mobile app version

---

[1.0.0]: https://github.com/horysheeet/NumericalMethods/releases/tag/v1.0.0
[Unreleased]: https://github.com/horysheeet/NumericalMethods/compare/v1.0.0...HEAD
