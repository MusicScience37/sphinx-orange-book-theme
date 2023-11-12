# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import pathlib

import toml

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


def read_version() -> str:
    """Read version from pyproject.toml file.

    Returns:
        str: Version.
    """
    this_dir = pathlib.Path(__file__).absolute().parent
    root_dir = this_dir.parent.parent
    pyproject_toml_path = root_dir / "pyproject.toml"
    config = toml.load(str(pyproject_toml_path))
    version = str(config["tool"]["poetry"]["version"])
    return version


project = "sphinx-orange-book-theme"
copyright = "2023, Kenta Kabashima"
author = "Kenta Kabashima"
release = read_version()

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ["_templates"]
exclude_patterns = []

# setting of todo
extensions += ["sphinx.ext.todo"]
todo_include_todos = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_orange_book_theme"
html_static_path = ["_static"]

html_title = "sphinx-orange-book-theme"

html_theme_options = {
    "repository_url": "https://gitlab.com/MusicScience37Projects/utility-libraries/sphinx-orange-book-theme",
    "use_repository_button": True,
}