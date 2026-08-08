# Day 60 - Find the Lexicographically Smallest Valid Sequence

## Problem

Given two strings `word1` and `word2`, find the lexicographically smallest sequence of indices in `word1` such that the selected characters form a string that is almost equal to `word2` (allowing at most one character to differ).

If no such sequence exists, return an empty array.

## Approach

The main challenge is obtaining the lexicographically smallest sequence while allowing exactly one possible mismatch.

I first scanned `word1` from right to left to determine the last possible position where every remaining character of `word2` could still be matched. This preprocessing tells me whether choosing a character now would still leave enough room to complete the sequence later.

Then I traversed `word1` from left to right.

- If the current characters matched, I selected the index.
- Otherwise, if I had not used my one allowed mismatch and the remaining suffix could still be matched, I greedily used the mismatch at the earliest possible position.

Since the sequence is built from left to right and the mismatch is only used when it is safe, the resulting index sequence is lexicographically smallest.

## Time Complexity

- **Time:** O(n + m)
- **Space:** O(m)

Where:

- `n` is the length of `word1`.
- `m` is the length of `word2`.

## What I Learned

- Reverse preprocessing can provide valuable information about future feasibility.
- Greedy algorithms often rely on knowing whether the remaining suffix can still be completed.
- Sometimes the lexicographically smallest answer is achieved by making an early decision, but only after proving it won't block the rest of the solution.