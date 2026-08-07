# Day 59 - Smallest Divisible Digit Product II

## Problem

Given a string `num` representing a positive integer and an integer `t`, find the smallest zero-free number greater than or equal to `num` such that the product of its digits is divisible by `t`. If no such number exists, return `"-1"`.

## Approach

This was one of the most challenging problems I've solved so far.

Instead of checking numbers one by one, I first decomposed `t` into its prime factors (2, 3, 5, and 7). If `t` contained any other prime factor, the answer was immediately impossible.

Next, I represented each digit by the prime factors it contributes. This allowed me to compare the factors required by `t` with the factors already available in the current number.

Starting from the rightmost digit, I tried replacing it with the next larger digit. After each replacement, I checked whether the remaining positions were sufficient to satisfy the missing prime factors. If they were, I filled the remaining positions with the lexicographically smallest valid digits.

If no valid number of the same length existed, I constructed the smallest valid number with one extra digit.

## Time Complexity

- **Time:** O(n)
- **Space:** O(1)

Where `n` is the length of the input string.

## What I Learned

- Prime factorization can transform a difficult digit-product problem into a counting problem.
- Greedy construction becomes much easier when you know exactly which factors are still required.
- Combining factor counts (such as using 8 instead of three 2's or 9 instead of two 3's) helps minimize both the length and lexicographical order of the answer.
- This was the toughest LeetCode problem I've solved so far and taught me how powerful number theory and greedy algorithms can be when used together.