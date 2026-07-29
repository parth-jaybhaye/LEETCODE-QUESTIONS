# Day 50 - Smallest Palindromic Rearrangement II

## Problem

In this problem, we are given a palindromic string and an integer `k`. We need to return the `k`-th lexicographically smallest palindromic rearrangement of the string. If there are fewer than `k` distinct palindromes, we return an empty string.

## Approach

Since every palindrome is determined by its left half, I first counted the frequency of each character. From these frequencies, I built the left half of the palindrome and identified the middle character (if one exists).

Before constructing the answer, I calculated the total number of distinct palindromic rearrangements. If `k` is larger than this count, I returned an empty string.

To build the left half, I tried placing each possible character in lexicographical order. After choosing a character, I calculated how many valid arrangements could still be formed with the remaining characters.

- If the number of arrangements was at least `k`, I kept that character.
- Otherwise, I skipped those arrangements, decreased `k` accordingly, and tried the next character.

Once the left half was complete, I added the middle character and then appended the reverse of the left half to form the final palindrome.

## Time Complexity

- Time: O(26 × n)
- Space: O(26)

## What I Learned

- A palindrome is completely determined by its left half.
- Combinatorics can be used to count permutations without generating them.
- Building the answer greedily works when we know how many arrangements each choice can produce.
- Counting arrangements first helps avoid unnecessary computation when `k` is too large.