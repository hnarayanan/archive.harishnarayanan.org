#!/usr/bin/env bash

rm `find ~harish/www_docs/ -name '*~' | xargs`
rm `find ~harish/www_docs/ -name '*pyc' | xargs`
