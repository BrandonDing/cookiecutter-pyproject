#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath: str) -> None:
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(filepath: str) -> None:
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath))


def copy_file(source: str, destination: str) -> None:
    shutil.copy(os.path.join(PROJECT_DIRECTORY, source), os.path.join(PROJECT_DIRECTORY, destination))


if __name__ == "__main__":
    if "{{cookiecutter.include_github_actions}}" != "y":
        remove_dir(".github")
    else:
        if "{{cookiecutter.mkdocs}}" != "y" and "{{cookiecutter.publish_to}}" == "none":
            remove_file(".github/workflows/on-release-main.yml")

    if "{{cookiecutter.mkdocs}}" != "y":
        remove_dir("docs")
        remove_file("mkdocs.yml")

    if "{{cookiecutter.dockerfile}}" != "y":
        remove_file("Dockerfile")

    if "{{cookiecutter.codecov}}" != "y":
        remove_file("codecov.yaml")
        if "{{cookiecutter.include_github_actions}}" == "y":
            remove_file(".github/workflows/validate-codecov-config.yml")

    if "{{cookiecutter.devcontainer}}" == "none":
        remove_dir(".devcontainer")
    elif "{{cookiecutter.devcontainer}}" == "python":
        remove_file(".devcontainer/docker-compose.yml")

    if "{{cookiecutter.configuration}}" == "n":
        remove_file("settings.yaml")
        if "{{cookiecutter.logging}}" == "none":
            remove_file("{{cookiecutter.project_slug}}/utils.py")
            remove_file("tests/test_utils.py")

    if "{{cookiecutter.python_version}}" == "ALL":
        copy_file(".devcontainer/Dockerfile-ubuntu", ".devcontainer/Dockerfile")
    else:
        copy_file(".devcontainer/Dockerfile-python", ".devcontainer/Dockerfile")
    remove_file(".devcontainer/Dockerfile-ubuntu")
    remove_file(".devcontainer/Dockerfile-python")
