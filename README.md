# Cookiecutter Pypackage Template

[![License](https://img.shields.io/github/license/mspronesti/pypackage-template)](https://opensource.org/licenses/Apache-2.0)

**Plug-and-play** cookiecutter template for creating a new Python library (or simply a tested, documented
and deployable package).

## TL; DR

All you got to do is clicking on the "Use this template" green button and and you are going to end up with a complete Python
package named after your project.

## Motivation

There are plenty of cookiecutter templates out there, but all of them require configuring your package by hand,
installing cookiecutter, the dependencies, generating the template and so on. 

This template attempts to address "the problem", aiming at providing a plug-and-play solution for lazy people like me.

## Features
* testing setup with `pytest`
* Github workflows for continuous integration testing
* [Sphinx](https://www.sphinx-doc.org/en/master/) docs ready for generation, further simplified through a Makefile
* Auto-release to [PyPI](https://pypi.org/) when you push a new tag to master, with **dynamic update of the version/tag number** (no need to update any file!)
* some common style-guidelines already setup for usage


## Publishing your library as a package to PyPI

To use this action, you need to create a PyPI account and an API token against that account.

Once you did, add that token to your repository as a GitHub secret called `PYPI_TOKEN` (don't change this name!). 

under `Settings > Secrets > New Secret` and you're done. 

From now on, any time you create a new Release or push a new tag on GitHub, the action will trigger, building your package and pushing it to PyPI.

The version number is gonna be updated automatically and only depends on the numbering of your release/tag.

## Documentation

Run 
```bash
Make apidoc
```
to produce the `rst` files and
```bash
Make doc
```
to produce the documentation.

