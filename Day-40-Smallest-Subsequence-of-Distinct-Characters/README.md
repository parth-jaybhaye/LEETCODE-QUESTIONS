# Day 40 - Smallest Subsequence of Distinct Characters

## Problem

In this problem, we are given a string and need to build the lexicographically smallest subsequence that contains every distinct character exactly once.

The challenge is to decide which characters to keep and which ones to remove while making sure every unique character still appears in the final answer.

## Approach

I used a greedy approach with a stack.

First, I stored the last occurrence of every character in the string. This helps determine whether a character can be removed now and added again later.

Then, I traversed the string one character at a time.

- If the current character was already included in the answer, I skipped it.
- Otherwise, I checked the top of the stack. While the stack was not empty, the top character was lexicographically larger than the current character, and it appeared again later in the string, I removed it from the stack.
- After removing all such characters, I added the current character to the stack and marked it as visited.

At the end, joining all the characters in the stack gives the required subsequence.

This approach ensures that every distinct character appears exactly once while keeping the result as small as possible in lexicographical order.

## Time Complexity

- Time: O(n)
- Space: O(n)

## What I Learned

- How a monotonic stack can be used to build the best possible sequence.
- Why storing the last occurrence of each character is useful.
- How a greedy approach can guarantee the lexicographically smallest answer.
- How a set helps avoid adding duplicate characters to the result.