# Python Essentials Labs

## Index
- [Introduction](#item_zero)
- [Files and Folders](#item_one)
    - [src](#item_one.zero)
    - [testing](#item_one.one)
    - [test.sh](#item_one.two)
- [Labs](#item_two)
    - [3.2.14 Essentials of the *while* loop](#item_two.zero)
    - [3.2.15 Collatz's hypothesis](#item_two.one)
    - [3.6.6 Operating with Lists - Basics](#item_two.two)
    - [4.3.4 A leap year](#item_two.three)
    - [4.3.6 Day of the year](#item_two.four)
    - [4.3.7 Prime numbers](#item_two.five)

## Introduction
This repository is a collection of the Lab Exercises and my solutions to each problem.
I have also added a script in bash to check if the solution is correct.

## Files and Folders

<a id="item_one.zero"></a>
### src

This folder includes the source code of the Labs.

<a id="item_one.one"></a>
### testing

This folder contains different cases for each lab to test if the solution provided in src/ is correct.

<a id="item_one.two"></a>
### test.sh

This is a script design to test each solution. To us it you will need to execute the following command:

        ./test.sh <name-of-the-lab>

<a id="item_two.zero"></a>
## 3.2.14 Essentials of the *while* loop

**Problem:** a boy and his father, a computer programmer, are playing with wooden blocks. They are building a pyramid.

Their pyramid is a bit weird, as it is actually a pyramid-shaped wall – it's flat. The pyramid is stacked according to one simple principle: each lower layer contains one block more than the layer above.

Your task is to write a program which reads the number of blocks the builders have, and outputs the height of the pyramid that can be built using these blocks.

Note: the height is measured by the number of fully completed layers – if the builders don't have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately.

**Solution:** src/pyramid.py

<a id="item_two.one"></a>
## 3.2.15 Collatz's hypothesis

**Problem:** In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis (it still remains unproven) which can be described in the following way:

1. take any non-negative and non-zero integer number and name it **c0**;
2. if it's even, evaluate a new **c0** as **c0** ÷ 2;
3. otherwise, if it's odd, evaluate a new **c0** as 3 × **c0** + 1;
4. if **c0** ≠ 1, go back to point 2.

The hypothesis says that regardless of the initial value of **c0**, it will always go to 1.

Write a program which reads one natural number and executes the above steps as long as **c0** remains different from 1. We also want you to count the steps needed to achieve the goal. Your code should output all the intermediate values of **c0**, too.

**Solution:** src/collatz.py

<a id="item_two.two"></a>
## 4.3.4 Operating with Lists - Basics

**Problem**: Imagine a list ‒ not very long, not very complicated, just a simple list containing some integer numbers. 
Some of these numbers may be repeated, and this is the clue. We don't want any repetitions. We want them to be removed.

Your task is to write a program which removes all the number repetitions from the list. The goal is to have a list in which all the numbers appear not more than once.

**Solution** src/no-repetition-list.py

<a id="item_two.three"></a>
## 4.3.6 Leap years

**Problem**: Write a function that returns True if a year is a *leap year* and False otherwise.

**Solution**: src/leap_years.py

<a id="item_two.four"></a>
## 4.3.7 Day of the year

**Problem**: Write a function that given three arguments (year, month, day of the month), returns the corresponding day of the year and None if it the arguments
are invalid.

**Solution**: src/day_of_the_year.py

<a id="item_two.five"></a>
## Prime numbers

**Problems**: Write a function that returns True if a number is prime and False otherwise.

**Solution**: src/prime_numbers.py