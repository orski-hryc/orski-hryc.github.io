#!/usr/bin/env bash

tree \
    --gitignore \
    -H . \
    -o index.html

cat index.html | sed 's/\.\.\//\/files\//g' > tmpfile
mv tmpfile index.html
