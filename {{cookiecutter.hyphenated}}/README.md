# {{ cookiecutter.hyphenated }}

[![PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.hyphenated }}.svg)](https://pypi.org/project/{{ cookiecutter.hyphenated }}/){% if cookiecutter.github_username %}
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.hyphenated }}/blob/main/LICENSE){% endif %}

{{ cookiecutter.description }}

## Installation

Install this library using `pip`:

    $ pip install {{ cookiecutter.hyphenated }}


## Development Notes

To contribute to this project, create a new virtual environment as follows:

    cd {{ cookiecutter.hyphenated }}
    python -m venv .venv
    source .venv/bin/activate

Now install the development dependencies

    pip install -r requirements-dev.txt

and run the tests:

    make test
