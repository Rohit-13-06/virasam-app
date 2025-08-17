# Contributing to VIRASAM: The Living Cultural Archive

Thank you for helping preserve and enrich our cultural heritage!  
This document outlines how you can contribute to the VIRASAM platform, covering code, documentation, and cultural content.

---

## 🏁 Table of Contents

- [Ways to Contribute](#ways-to-contribute)
- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Reporting Issues](#reporting-issues)
- [Suggesting Features](#suggesting-features)
- [Coding Guidelines](#coding-guidelines)
- [Pull Requests](#pull-requests)
- [Cultural Content Guidelines](#cultural-content-guidelines)
- [Translations](#translations)
- [Getting Help](#getting-help)
- [Acknowledgments](#acknowledgments)

---

## 🌟 Ways to Contribute

- Report bugs or issues
- Suggest improvements or new features
- Submit code (bugfixes, new features, tests)
- Improve documentation
- Contribute stories, traditions, recipes, or media
- Add translations/localizations

---

## 🤝 Code of Conduct

We are committed to a welcoming and respectful environment for all cultural backgrounds, languages, and levels of technical experience.  
By participating, you agree to uphold the [Contributor Covenant](https://www.contributor-covenant.org/version/2/1/code_of_conduct/).

---

## 🚦 How to Contribute

1. **Fork this repository** and clone to your local machine.
2. **Create a branch**:  
   `git checkout -b feature/feature-name` or `fix/issue-description`
3. **Install dependencies**:  
   `pip install -r requirements.txt`
4. **Make your changes**  
   - Code in Python: keep it readable and well-commented.
   - For documentation or cultural content, use clear language and appropriate file locations.
5. **Test locally**:  
   `streamlit run frontend/app.py`
6. **Ensure code style**:  
   - Format Python code with `black`.
   - Lint using `ruff` (`pip install ruff`, then `ruff .`)
7. **Commit with clear messages**  
   Example:  
   `git commit -m "feat: add traditional Bengali recipes page"`
8. **Push to your fork**:  
   `git push origin feature/feature-name`
9. **Open a Merge Request** ([Merge Requests](/-/merge_requests))  
   - Fill out PR template and reference related issues if any.

---

## 🐛 Reporting Issues

1. Use the issue templates in `.gitlab/issue_templates/` for:
    - Bug reports
    - Feature requests
    - Documentation suggestions
2. Provide as much detail as possible:
    - Environment (OS, browser, Python version)
    - Steps to reproduce
    - Expected and actual behavior
    - Screenshots or logs if helpful

---

## 💡 Suggesting Features

- Use the "Feature.md" issue template.
- State the problem, your proposal, and possible alternatives.
- Describe user stories or examples when appropriate.

---

## 📝 Coding Guidelines

- **PEP8** and **Black** for Python style
- **Ruff** for linting
- Use type hints wherever possible
- Add docstrings to functions/classes
- Keep functions/classes short and focused
- Write tests for new or changed code

---

## 🚀 Pull Requests

- Reference related issues by number in your PR (`Closes #IssueNo`)
- Complete all PR checklist items:
    - [ ] Code is documented
    - [ ] Passes linting and tests
    - [ ] No secrets or hardcoded credentials
    - [ ] User-facing text is internationalized (use `_()` where needed)
- If your PR changes the UI or user experience, please add screenshots.
- Ensure your PR only does **one thing** – split into multiple PRs if needed.

---

## 🌍 Cultural Content Guidelines

- Please include relevant background: region, language, tradition, date, etc.
- Respect all communities and cultural sensitivities.
- Cite sources for factual/historical information when possible.
- Only upload content/media you have the right to share and license under AGPLv3.
- All community content contributions are public and open-licensed.

---

## 🌐 Translations

- To add a new language or improve translation, work in `frontend/utils/translation.py`.
- All UI strings should use the `_()` function (already prepared).
- Check that translated strings fit in the UI and maintain meaning.

---

## 🤔 Getting Help

- For general questions, open a [discussion](https://code.swecha.org/yourusername/virasam-app/-/discussions) or issue
- See the [README.md](README.md) for setup instructions
- Contact maintainers at support@virasam.org

---

## 🙇 Acknowledgments

Thank you for making VIRASAM a living archive of culture.  
Everyone’s contribution matters – from one line of code to the preservation of an ancient story.

---

*VIRASAM is open to all cultures, backgrounds, and languages. Let’s build this archive together!*
