#!/bin/sh

pip install -r requirements.txt

rm -rf ./build && \
cp ./preview_configuration.py ./conf.py && \

cd ../docs/it
sphinx-build . build -c .
