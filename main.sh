#!/bin/bash

if [ $# -ge 1 ]; then
    echo '# ------------------------------------------------'
    echo '# Fetch data.'
    echo '# ------------------------------------------------'
    # data sans-ts > /dev/null
    data avec-ts > /dev/null
    echo
    echo
fi

echo '# ------------------------------------------------'
echo '# R script.'
echo '# ------------------------------------------------'
(cd R; ./main.r)
echo
echo

echo '# ------------------------------------------------'
echo '# Python script.'
echo '# ------------------------------------------------'
(cd python; ./main.py)
