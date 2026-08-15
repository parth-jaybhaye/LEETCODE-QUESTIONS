# Day 67 - Longest Subsequence With Non-Zero Bitwise XOR

## Problem

Given an integer array `nums`, find the length of the longest subsequence whose bitwise XOR is non-zero.

If no such subsequence exists, return `0`.

## Approach

I first computed the XOR of all elements in the array.

- If the total XOR is already non-zero, then the entire array forms the longest valid subsequence.
- Otherwise, the total XOR is zero. In this case, removing any non-zero element changes the overall XOR, making it non-zero. Therefore, if there is at least one non-zero element, the answer is `n - 1`.
- If every element is `0`, then every possible subsequence also has XOR equal to `0`, so the answer is `0`.

This observation avoids any dynamic programming or backtracking and leads to a simple linear-time solution.

## Time Complexity

- Time: **O(n)**
- Space: **O(1)**

## What I Learned

- Sometimes a problem that appears to require subsequence DP can be solved using properties of the XOR operation.
- The XOR of the entire array provides enough information to determine the optimal answer.
- Understanding mathematical properties of bitwise operations can greatly simplify seemingly difficult problems.