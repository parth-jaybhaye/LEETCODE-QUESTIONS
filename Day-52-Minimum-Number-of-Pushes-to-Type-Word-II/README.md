# Day 52 - Minimum Number of Pushes to Type Word II

## Problem

In this problem, we are given a word containing lowercase English letters. We can remap the letters to the phone keypad in any way we want. The goal is to minimize the total number of key presses needed to type the entire word.

Unlike the previous version, characters can appear multiple times, so assigning frequently used letters to positions with fewer key presses becomes important.

## Approach

I first counted the frequency of every character using `Counter`.

Then, I sorted the frequencies in descending order so that the most frequent characters are considered first.

A phone keypad has 8 available keys, so:

- The first 8 most frequent characters need only 1 push.
- The next 8 characters need 2 pushes.
- The next 8 need 3 pushes, and so on.

For each frequency, I calculated its required push count using `i // 8 + 1`, where `i` is its position after sorting.

Finally, I multiplied each frequency by its push count and added all the values to get the minimum number of key presses.

This greedy approach works because assigning the most frequent characters to the lowest push counts always minimizes the total cost.

## Time Complexity

- Time: O(n + k log k)
- Space: O(k)

Where:
- `n` is the length of the word.
- `k` is the number of distinct characters (at most 26).

## What I Learned

- Greedy strategies are useful when we need to minimize a weighted cost.
- Sorting character frequencies helps assign the cheapest positions to the most frequent letters.
- `Counter` makes frequency counting very simple.
- Sometimes two different problems can have the same optimal solution even if their constraints are different.