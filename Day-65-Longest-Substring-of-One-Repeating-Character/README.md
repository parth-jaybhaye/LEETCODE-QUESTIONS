# Day 63 - Longest Substring of One Repeating Character

## Problem

You are given a string `s` and a list of update queries. Each query changes one character in the string.

After every update, determine the length of the longest substring consisting of only one repeating character.

## Approach

Since each query updates a single character and asks for the maximum repeating substring, recalculating the answer after every update would be too slow.

To solve this efficiently, I used a **Segment Tree**.

Each node of the segment tree stores:

- The longest repeating substring inside its range.
- The repeating prefix length and its character.
- The repeating suffix length and its character.
- The maximum repeating character and its length.

When two child nodes are merged:

- The maximum repeating substring is taken from either child or formed by combining the left suffix and right prefix if they contain the same character.
- Prefix and suffix information are updated accordingly.

For every query, only the nodes along the update path are modified, making each update efficient.

## Time Complexity

- Building the Segment Tree: **O(n)**
- Each Update Query: **O(log n)**
- Total: **O(n + q log n)**

Where:

- `n` is the length of the string.
- `q` is the number of queries.

## Space Complexity

- **O(n)**

## What I Learned

- Segment Trees can maintain complex information instead of just sums or minimums.
- Carefully designing what each node stores allows efficient range merging.
- This problem is a great example of combining multiple pieces of information (prefix, suffix, and maximum) to answer dynamic string queries efficiently.
- One-character updates can be handled in logarithmic time with the right data structure.