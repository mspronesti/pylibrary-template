import setuptools
import os


# loading requirements from textfile
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()



setuptools.setup(
    name="{{ cookiecutter.hyphenated }}",
    description="{{ cookiecutter.description }}",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",{% if cookiecutter.author_name %}
    author="{{ cookiecutter.author_name }}",{% endif %}{% if cookiecutter.github_username %}
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.hyphenated }}",
    project_urls={
        "Issues": "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.hyphenated }}/issues",
        "CI": "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.hyphenated }}/actions",
        "Changelog": "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.hyphenated }}/releases",
    },{% endif %}
    license="Apache License, Version 2.0",
    packages=["{{ cookiecutter.underscored }}"],
    install_requires=requirements,
    python_requires=">=3.7"
)