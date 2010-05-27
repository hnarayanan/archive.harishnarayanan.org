#!/usr/bin/env bash

for file in ${1}/*.jpg
do
    echo "('"${file}"', '"`dirname ${file}`"/thumbnails/"`basename ${file}`"'),"
done