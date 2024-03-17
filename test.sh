#!/bin/bash

check(){
    read RED
    if [[ "$RED" = "$1" ]]; then
        return 0
    else
        return 1
    fi
}

INPUT=(1 2 3 6 8 20 1000)
OUTPUT=(1 1 2 3 3 5 44)
TEST_LENGHT=${#INPUT[@]}

fails=0
ind=0
for ((; !$fails && ind<TEST_LENGHT; ind++))
do
    echo ${INPUT[ind]} | python pyramid.py | check "Enter the number of blocks: The height of the pyramid: ${OUTPUT[ind]}"
    fails=$?
done

if [ $fails -eq 1 ]; then
    echo "test fails at index $((ind-1))" >&2
    exit 1
else
    exit 0
fi