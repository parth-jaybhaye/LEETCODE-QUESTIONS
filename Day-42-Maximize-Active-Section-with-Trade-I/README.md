# Day 42 - Maximize Active Section with Trade I

## Problem

In this problem, we are given a binary string where `1` represents an active section and `0` represents an inactive section. We can perform at most one trade to maximize the number of active sections.

The trade consists of first changing one valid block of `1`s into `0`s and then changing one valid block of `0`s into `1`s. The goal is to find the maximum number of active sections after the best possible trade.

## Approach

I started by adding a `1` at both ends of the string. This makes it easier to handle the boundary cases because every valid block can be treated in the same way.

Next, I used `groupby` to find the lengths of all continuous blocks of `0`s in the modified string.

The main idea is that two consecutive zero blocks can be connected by removing the block of `1`s between them. So, I checked every pair of adjacent zero groups and kept track of the largest combined length.

Finally, I counted the number of active sections already present in the original string and added the best increase found from merging two zero groups.

This approach avoids simulating every possible trade and works efficiently even for large strings.

## Time Complexity

- Time: O(n)
- Space: O(n)

## What I Learned

- How adding sentinel values can simplify edge cases.
- How `itertools.groupby` helps process consecutive characters easily.
- How observing the pattern in grouped sections can avoid complicated simulations.
- Looking for the right observation can lead to a much simpler solution.