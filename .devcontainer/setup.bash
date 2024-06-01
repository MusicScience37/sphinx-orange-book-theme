#!/bin/bash

poetry config virtualenvs.in-project true
poetry env use 3.12
poetry install

poetry run pre-commit install

git config gpg.program gpg2
git config commit.gpgsign true
git config tag.gpgsign true

git lfs install

echo "source /usr/share/bash-completion/completions/git" >> ~/.bashrc
