# Day 49 - Smallest Palindromic Rearrangement I

## Problem

In this problem, we are given a palindromic string. We need to rearrange its characters to form the lexicographically smallest palindrome possible.

Since the input is already guaranteed to be a palindrome, we know that a valid palindromic rearrangement always exists.

## Approach

The key observation is that the second half of a palindrome is completely determined by the first half.

I first took the first half of the string and sorted it in ascending order. Sorting this half ensures that the palindrome starts with the smallest possible characters, making the entire string lexicographically smallest.

If the length of the string is odd, I kept the middle character unchanged because it always remains at the center of the palindrome.

Finally, I created the answer by combining:
- the sorted first half,
- the middle character (only if the length is odd),
- the reverse of the sorted first half.

This directly constructs the smallest possible palindrome without generating all permutations.

## Time Complexity

- Time: O(n log n)
- Space: O(n)

## What I Learned

- A palindrome is completely determined by its first half.
- Sorting the first half is enough to get the lexicographically smallest palindrome.
- The middle character of an odd-length palindrome never changes its position.
- Understanding the properties of a problem can lead to a very short and clean solution.