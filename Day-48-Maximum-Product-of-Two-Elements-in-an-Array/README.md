# Day 48 - Maximum Product of Two Elements in an Array

## Problem

In this problem, we are given an array of integers. We need to choose two different elements and return the maximum value of `(nums[i] - 1) * (nums[j] - 1)`.

The goal is to find the best pair without checking every possible combination.

## Approach

Instead of sorting the entire array, I kept track of the two largest numbers while traversing the array only once.

I used two variables:

- `max1` stores the largest number seen so far.
- `max2` stores the second largest number.

For each number:

- If it is greater than `max1`, I update both `max1` and `max2`.
- Otherwise, if it is greater than `max2`, I only update `max2`.

After finding the two largest numbers, I directly calculate `(max1 - 1) * (max2 - 1)` and return the result.

This approach avoids sorting and solves the problem in a single pass.

## Time Complexity

- Time: O(n)
- Space: O(1)

## What I Learned

- How to find the two largest elements in one traversal.
- A single-pass solution can be more efficient than sorting.
- Keeping track of the largest and second largest values is a common interview technique.
- Always look for ways to reduce unnecessary work when only a few values are needed.