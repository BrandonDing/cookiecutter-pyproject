# Cookiecutter Pyproject

---

[![Release](https://img.shields.io/github/v/release/BrandonDing/cookiecutter-pyproject)](https://pypi.org/project/cookiecutter-pyproject/)
[![Build status](https://img.shields.io/github/actions/workflow/status/BrandonDing/cookiecutter-pyproject/main.yml?branch=main)](https://github.com/BrandonDing/cookiecutter-pyproject/actions/workflows/main.yml?query=branch%3Amain)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/cookiecutter-pyproject)](https://pypi.org/project/cookiecutter-pyproject/)
[![Docs](https://img.shields.io/badge/docs-gh--pages-blue)](https://BrandonDing.github.io/cookiecutter-pyproject/)
[![License](https://img.shields.io/github/license/BrandonDing/cookiecutter-pyproject)](https://img.shields.io/github/license/BrandonDing/cookiecutter-pyproject)


This is a modern Cookiecutter template that can be used to initiate a Python project with all the necessary tools for development, testing, and deployment. It supports the following features:

- [Poetry](https://python-poetry.org/) for dependency management
- [ Dev Container ](https://code.visualstudio.com/docs/devcontainers/containers) for full-featured development environment
- CI/CD with [GitHub Actions](https://github.com/features/actions)
- Pre-commit hooks with [pre-commit](https://pre-commit.com/)
- Code quality with [black](https://pypi.org/project/black/), [ruff](https://github.com/charliermarsh/ruff), [mypy](https://mypy.readthedocs.io/en/stable/), and [deptry](https://github.com/BrandonDing/deptry/)
- Publishing to [Pypi](https://pypi.org) or [Artifactory](https://jfrog.com/artifactory) by creating a new release on GitHub
- Testing and coverage with [pytest](https://docs.pytest.org/en/7.1.x/) and [codecov](https://about.codecov.io/)
- Documentation with [MkDocs](https://www.mkdocs.org/)
- Compatibility testing for multiple versions of Python with [Tox](https://tox.wiki/en/latest/)
- Containerization with [Docker](https://www.docker.com/)
- [ Dynaconf ](https://www.dynaconf.com/) for configuration management
- Enjoyable logging with [ Loguru ](https://loguru.readthedocs.io/en/stable/overview.html)

---
<p align="center">
  <a href="https://BrandonDing.github.io/cookiecutter-pyproject/">Documentation</a> - <a href="https://github.com/BrandonDing/cookiecutter-pyproject-example">Example</a> -
  <a href="https://pypi.org/project/cookiecutter-pyproject/">PyPi</a>
</p>

---




## Quickstart

On your local machine, navigate to the directory in which you want to
create a project directory, and run the following two commands:

``` bash
pip install cookiecutter-pyproject 
ccp
```

Alternatively, install `cookiecutter` and directly pass the URL to this
Github repository to the `cookiecutter` command:

``` bash
pip install cookiecutter
cookiecutter https://github.com/BrandonDing/cookiecutter-pyproject.git
```

Create a repository on GitHub, and then run the following commands, replacing `<project-name>`, with the name that you gave the Github repository and
`<github_author_handle>` with your Github username.

``` bash
cd <project_name>
git init -b main
git add .
git commit -m "Init commit"
git remote add origin git@github.com:<github_author_handle>/<project_name>.git
git push -u origin main
```

Finally, install the environment and the pre-commit hooks with

 ```bash
 make install
 ```

You are now ready to start development on your project! The CI/CD
pipeline will be triggered when you open a pull request, merge to main,
or when you create a new release.

To finalize the set-up for publishing to PyPi or Artifactory, see
[here](https://BrandonDing.github.io/cookiecutter-pyproject/features/publishing/#set-up-for-pypi).
For activating the automatic documentation with MkDocs, see
[here](https://BrandonDing.github.io/cookiecutter-pyproject/features/mkdocs/#enabling-the-documentation-on-github).
To enable the code coverage reports, see [here](https://BrandonDing.github.io/cookiecutter-pyproject/features/codecov/).

## Acknowledgements

This project is partially based on [Florian Maas](https://github.com/fpgmaas)\'s great
[cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry)
repository.
