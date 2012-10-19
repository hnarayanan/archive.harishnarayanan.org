#!/usr/bin/env bash

for file in `find . -name *.png`
do
    pngout ${file}
done
