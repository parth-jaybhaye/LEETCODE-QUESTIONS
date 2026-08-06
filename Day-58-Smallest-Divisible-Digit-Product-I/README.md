# Day 58 - Smallest Divisible Digit Product I

## Problem

Given two integers `n` and `t`, find the smallest integer greater than or equal to `n` whose product of digits is divisible by `t`.

## Approach

Since the constraints guarantee that the answer will be found within the next few numbers, I simply checked every number starting from `n`.

For each candidate number, I computed the product of its digits using a helper function. As soon as I found a number whose digit product was divisible by `t`, I returned it immediately.

This straightforward brute-force approach is both simple and efficient because the search range is very small.

## Time Complexity

- Time: **O(1)**
- Space: **O(1)**

The algorithm checks at most 10 numbers, and each number has only a few digits.

## What I Learned

- Always pay attention to the constraints before looking for complex optimizations.
- Sometimes a brute-force solution is the intended solution when the input size is tightly bounded.
- Separating repeated logic into a helper function keeps the main solution clean and easy to read.