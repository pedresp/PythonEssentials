#!/bin/bash

check(){
    read RED
    if [[ "$RED" = "$1" ]]; then
        return 0
    else
        return 1
    fi
}

if [ $# -ne 1 ]; then
    echo "bad argument" >&2
    exit 2
fi

fails=0
ind=0

case $1 in
    "pyramid")
        INPUT=(1 2 3 6 8 20 1000)
        OUTPUT=(1 1 2 3 3 5 44)
        TEST_LENGHT=${#INPUT[@]}

        for ((; !$fails && ind<TEST_LENGHT; ind++))
        do
            echo ${INPUT[ind]} | python src/pyramid.py | check "Enter the number of blocks: The height of the pyramid: ${OUTPUT[ind]}"
            fails=$?
        done;;
    
    "collatz")
        INPUT=(15 16 1023)
        TEST_LENGHT=${#INPUT[@]}

        for ((; !fails && ind<TEST_LENGHT; ind++))
        do
            echo ${INPUT[ind]} | python src/collatz.py > file
            diff file "testing/collatz/test$ind.txt"
            fails=$?
        done

        rm file;;
    *)
        echo "incorrect test name" >&2
        exit 3;;
esac

if [ $fails -eq 1 ]; then
    echo "tests fail at index $((ind-1))" >&2
    exit 1
else
    echo "tests for $1 ran correctly"
    exit 0
fi