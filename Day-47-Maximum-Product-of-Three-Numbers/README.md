# Day 47 - Maximum Product of Three Numbers

## Problem

In this problem, we are given an integer array. We need to find the maximum product that can be obtained by multiplying any three numbers from the array.

The array may contain both positive and negative numbers, so we need to consider different possible combinations.

## Approach

I first sorted the array in ascending order.

After sorting, there are two possible ways to get the maximum product:

- Multiply the three largest numbers.
- Multiply the two smallest numbers (which could both be negative) with the largest number.

The second case is important because the product of two negative numbers is positive. Sometimes, this product can be larger than using the three largest positive numbers.

Finally, I calculated both values and returned the larger one using the `max()` function.

This approach is simple and correctly handles arrays containing both positive and negative values.

## Time Complexity

- Time: O(n log n)
- Space: O(1)

## What I Learned

- Sorting makes it easy to compare the possible maximum product combinations.
- Negative numbers can increase the final product when multiplied together.
- It is important to consider edge cases instead of assuming the largest numbers always give the best answer.
- Sometimes checking only a few carefully chosen cases is enough to solve the problem.