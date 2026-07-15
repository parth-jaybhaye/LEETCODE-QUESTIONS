# Day 018 - Find the Maximum Number of Elements in a Subset

## Problem

Given an array of positive integers, select the largest possible subset that can be arranged in the following pattern:

`[x, x², x⁴, ..., xᵏ, ..., x⁴, x², x]`

where every value except the middle one must appear twice.

Return the maximum size of such a subset.

## Approach

I first counted the frequency of every number using a hash map.

For every possible starting value (except `1`), I repeatedly squared the current number and checked whether it appeared at least twice. If it did, I could place one copy on the left side and one on the right side of the pattern.

This process continued until I could no longer extend the chain.

At the end:
- If the final squared value existed, it could be placed once in the middle.
- Otherwise, the previous value became the middle element, reducing the total length by one.

The value `1` is handled separately because squaring `1` always gives `1`. The longest valid sequence of `1`s must contain an odd number of elements.

The maximum length over all possible starting values is the answer.

## Complexity

- Time Complexity: **O(n log log M)** (approximately), where `M` is the maximum value in the array.
- Space Complexity: **O(n)**

## What I Learned

- Practiced using a frequency map to count occurrences efficiently.
- Learned how repeated squaring forms chains that can be extended greedily.
- Improved my understanding of handling special cases like the value `1`.

## DSA Takeaway

The key observation is that every value except the middle element must appear twice. By extending square chains as long as possible using the frequency map, we can efficiently compute the largest valid subset.