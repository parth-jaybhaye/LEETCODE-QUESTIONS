# Day 44 - Number of Unique XOR Triplets I

## Problem

In this problem, we are given a permutation of numbers from `1` to `n`. We need to consider every possible triplet `(i, j, k)` where `i <= j <= k`, calculate the XOR of the three selected values, and return the number of unique XOR results.

At first, it feels like we need to check every possible triplet, but that would be too slow for the given constraints.

## Approach

This solution is based on a mathematical observation instead of checking all triplets.

If the array has fewer than three elements, the answer is simply the number of elements because no new XOR values can be formed.

For arrays with three or more elements, the unique XOR values always cover every number from `0` up to the next power of two minus one. The number of these values is equal to the next power of two greater than `n`.

Python's `bit_length()` function helps find this value. By calculating `1 << n.bit_length()`, we directly get the required count without generating any triplets.

This makes the solution extremely fast and uses only constant extra space.

## Time Complexity

- Time: O(1)
- Space: O(1)

## What I Learned

- Some XOR problems can be solved using mathematical properties instead of brute force.
- `bit_length()` is useful for finding the next power of two.
- Looking for patterns in the problem can lead to a much simpler solution.
- Not every problem requires simulating all possible combinations.