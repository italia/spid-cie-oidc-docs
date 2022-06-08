#!/bin/sh

rm -rf ./build && \
cp ./preview_configuration.py ./conf.py && \
sphinx-build ../docs/it build -c .
