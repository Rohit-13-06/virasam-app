# Contributing to VIRASAM

Thank you for your interest in contributing to VIRASAM! This document provides guidelines and information for contributors.

## 🎯 Types of Contributions

We welcome various types of contributions:

### Code Contributions
- Bug fixes and improvements
- New features and functionality
- Performance optimizations
- Documentation updates

### Cultural Content
- Traditional stories and folklore
- Historical information and events
- Traditional recipes and cooking methods
- Cultural practices and ceremonies

### Documentation
- README improvements
- Code documentation
- User guides and tutorials
- Translation and localization

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Git knowledge
- Basic understanding of Streamlit and Supabase

### Development Setup

1. **Fork the repository**
git clone https://github.com/yourusername/virasam-app.git
cd virasam-app

text

2. **Create a virtual environment**
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

text

3. **Install dependencies**
pip install -r requirements.txt
pip install -r requirements-dev.txt # Development dependencies

text

4. **Set up environment variables**
cp .streamlit/secrets.example.toml .streamlit/secrets.toml

Edit with your Supabase credentials
text

5. **Run tests**
pytest tests/

text

6. **Start development server**
streamlit run frontend/app.py

text

## 📝 Code Guidelines

### Python Code Style
- Follow [PEP 8](https://pep8.org/) style guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Maximum line length: 88 characters (Black formatter)

### Code Structure
def function_name(param1: str, param2: int) -> bool:
"""
Brief description of the function.

text
Args:
    param1: Description of parameter 1
    param2: Description of parameter 2
    
Returns:
    Description of return value
"""
# Implementation here
return True
text

### Database Operations
- Always use the provided database functions in `backend/database.py`
- Handle exceptions appropriately with user-friendly error messages
- Use UUID conversion functions for user IDs
- Follow the established pattern for database queries

### Frontend Guidelines
- Use Streamlit best practices for UI components
- Implement proper error handling with user feedback
- Maintain consistent styling and layout
- Add appropriate loading spinners for long operations

## 🔄 Development Workflow

### 1. Create a Feature Branch
git checkout -b feature/your-feature-name

text

### 2. Make Your Changes
- Write clean, documented code
- Add or update tests as necessary
- Update documentation if needed

### 3. Test Your Changes
Run all tests
pytest

Test specific functionality
python -m pytest tests/test_database.py

Run linting
flake8 .
black --check .

text

### 4. Commit Your Changes
git add .
git commit -m "feat: add new cultural content search feature"

text

### Commit Message Format
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes
- `refactor:` Code refactoring
- `test:` Test-related changes
- `chore:` Maintenance tasks

### 5. Push and Create Pull Request
git push origin feature/your-feature-name

text

## 🧪 Testing

### Running Tests
All tests
pytest

With coverage
pytest --cov=backend --cov=frontend

Specific test file
pytest tests/test_database.py -v

text

### Writing Tests
- Write unit tests for all new functions
- Include integration tests for database operations
- Test error handling and edge cases
- Mock external dependencies (Supabase, Ollama)

Example test:
import pytest
from backend.database import save_folk_contribution

def test_save_folk_contribution_success(mock_supabase):
# Arrange
mock_supabase.from_().insert().execute.return_value.data = [{"id": "test-id"}]

text
# Act
result = save_folk_contribution("user-1", "Test Title", "Test Description")

# Assert
assert len(result) == 1
assert result["id"] == "test-id"
text

## 📚 Documentation Standards

### Code Documentation
- Add docstrings to all public functions
- Include type hints for function parameters and returns
- Document complex algorithms or business logic
- Update README.md for new features

### API Documentation
- Document all database functions
- Include example usage
- Specify expected input/output formats
- Document error conditions

## 🌍 Cultural Content Guidelines

### Content Standards
- Respect cultural sensitivity and authenticity
- Provide proper attribution when possible
- Include regional or community context
- Avoid culturally appropriative content

### Content Format
- Use clear, descriptive titles
- Provide comprehensive descriptions
- Include relevant metadata (region, time period, etc.)
- Add media files when appropriate

### Quality Guidelines
- Fact-check historical information
- Verify traditional recipes and methods
- Include multiple perspectives when relevant
- Cite sources for historical claims

## 🐛 Bug Reports

### Before Submitting
1. Check existing issues for duplicates
2. Verify the bug exists in the latest version
3. Test with minimal reproduction steps

### Bug Report Template
Bug Description
A clear description of the bug.

Steps to Reproduce

Go to '...'

Click on '...'

See error

Expected Behavior
What you expected to happen.

Screenshots
If applicable, add screenshots.

Environment

OS: [e.g., Windows 10]

Python version: [e.g., 3.9.0]

Browser: [e.g., Chrome 95.0]

text

## 💡 Feature Requests

### Feature Request Template
Feature Description
A clear description of the proposed feature.

Problem Statement
What problem does this solve?

Proposed Solution
How should this feature work?

Alternatives Considered
Other solutions you've considered.

Additional Context
Screenshots, mockups, or examples.

text

## 🔍 Code Review Process

### For Contributors
- Ensure your code follows the style guidelines
- Write descriptive commit messages
- Add tests for new functionality
- Update documentation as needed

### Review Criteria
- Code quality and readability
- Test coverage and quality
- Documentation completeness
- Cultural sensitivity (for content)
- Performance implications

## 🏆 Recognition

Contributors will be recognized in:
- CHANGELOG.md for significant contributions
- README.md acknowledgments section
- Annual contributor highlights

## 📞 Getting Help

### Community Support
- **GitHub Discussions**: General questions and ideas
- **GitHub Issues**: Bug reports and feature requests
- **Email**: maintainers@virasam.org

### Development Questions
- Check existing documentation first
- Search previous issues and discussions
- Ask specific, detailed questions
- Provide relevant code snippets

## 📋 Checklist

Before submitting a pull request:

- [ ] Code follows style guidelines
- [ ] Tests pass locally
- [ ] Documentation is updated
- [ ] Commit messages are descriptive
- [ ] No sensitive data is included
- [ ] Cultural content is appropriate and respectful

## 🤝 Code of Conduct

This project follows a Code of Conduct to ensure a welcoming environment for all contributors. Please:

- Be respectful and inclusive
- Welcome newcomers and help them get started
- Respect cultural differences and sensitivities
- Focus on constructive feedback
- Report inappropriate behavior to maintainers

---

Thank you for contributing to VIRASAM! Together, we're preserving cultural heritage for future generations. 🌍