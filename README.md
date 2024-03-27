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

## Introduction
This repository is a collection of the Lab Exercises and my solutions to each problem.
I have also added a script in bash to check if the solution is correct.

<a id="item_two.zero"></a>
## 3.2.14 Essentials of the *while* loop

**Problem:** a boy and his father, a computer programmer, are playing with wooden blocks. They are building a pyramid.

Their pyramid is a bit weird, as it is actually a pyramid-shaped wall – it's flat. The pyramid is stacked according to one simple principle: each lower layer contains one block more than the layer above.

Your task is to write a program which reads the number of blocks the builders have, and outputs the height of the pyramid that can be built using these blocks.

Note: the height is measured by the number of fully completed layers – if the builders don't have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately.

**Solution:** pyramid.py

<a id="item_two.one"></a>
## 3.2.15 Collatz's hypothesis

**Problem:** In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis (it still remains unproven) which can be described in the following way:

1. take any non-negative and non-zero integer number and name it **c0**;
2. if it's even, evaluate a new **c0** as **c0** ÷ 2;
3. otherwise, if it's odd, evaluate a new **c0** as 3 × **c0** + 1;
4. if **c0** ≠ 1, go back to point 2.

The hypothesis says that regardless of the initial value of **c0**, it will always go to 1.

Write a program which reads one natural number and executes the above steps as long as **c0** remains different from 1. We also want you to count the steps needed to achieve the goal. Your code should output all the intermediate values of **c0**, too.

**Solution:** collatz.py