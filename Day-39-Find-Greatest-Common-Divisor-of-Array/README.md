# Day 39 - Find Greatest Common Divisor of Array

## Problem

In this problem, we are given an array of integers. We need to find the smallest and the largest number in the array, then return their greatest common divisor (GCD).

The task is simple because we only need to compare the minimum and maximum values instead of checking every element.

## Approach

My solution uses Python's built-in `min()` and `max()` functions to find the smallest and largest numbers in the array.

Once these two values are found, I use `math.gcd()` to calculate their greatest common divisor.

Since Python already provides an efficient implementation of the GCD function, the code becomes very short and easy to understand.

## Time Complexity

- Time: O(n)
- Space: O(1)

## What I Learned

- The GCD only needs to be calculated between the smallest and largest elements.
- Python's `min()` and `max()` functions make finding the required values simple.
- The built-in `math.gcd()` function is an efficient way to compute the greatest common divisor.
- Sometimes a problem can have a very clean solution by using the right built-in functions.