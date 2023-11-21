# sphinx-orange-book-theme

An orange version of [sphinx-book-theme](https://sphinx-book-theme.readthedocs.io/en/latest/index.html).

This python package overrides CSS of sphinx-book-theme
to change its design.

## Usage

To use this theme,

1. Install
   [sphinx-orange-book-theme](https://pypi.org/project/sphinx-orange-book-theme/)
   package from PyPI, for example, using the following command:

   ```shell
   pip install sphinx-orange-book-theme
   ```

2. Update your conf.py file to use `sphinx_orange_book_theme` theme as following:

   ```python
   html_theme = "sphinx_orange_book_theme"
   ```

3. (Recommended) Add following options to conf.py:

   ```python
   html_theme_options = {
       "pygment_light_style": "gruvbox-light",
       "pygment_dark_style": "native",
   }
   ```

   Although these options are not required to use this theme,
   this theme is designed with the above options.

## Documentation

- [Documentation built on main branch](https://sphinx-orange-book-theme-musicscience37projects--1dc46f9ab80e60.gitlab.io/)
