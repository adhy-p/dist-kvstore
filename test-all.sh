#!/bin/sh

flake8 src tests
mypy src
pytest
