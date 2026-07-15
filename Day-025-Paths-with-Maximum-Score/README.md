# Day 025 - Paths with Maximum Score

## Problem

You are given a square board containing:
- `E` → Starting point at the top-left.
- `S` → Ending point at the bottom-right.
- Numbers `1-9` → Points that can be collected.
- `X` → Obstacles that cannot be crossed.

You can move:
- Up
- Left
- Diagonally up-left

Return:
1. The maximum score that can be collected.
2. The number of paths that achieve this maximum score.

The number of paths should be returned modulo `10^9 + 7`.

## Approach

I used **Dynamic Programming**.

Since movement is only possible towards the top-left direction, I processed the board from bottom-right to top-left.

For every cell, I stored:
- Maximum score possible from that cell to reach `E`.
- Number of ways to achieve that maximum score.

For each cell:
- I checked the three possible previous positions.
- Took the maximum score among them.
- Added the number of paths from all directions that gave the same maximum score.
- Added the current cell value to the score.

If a cell is unreachable, it is ignored.

## Complexity

- Time Complexity: **O(n²)**
- Space Complexity: **O(n²)**

where `n` is the size of the board.

## What I Learned

- Practiced grid-based dynamic programming.
- Learned how to store both maximum values and number of ways.
- Improved understanding of path counting problems.

## DSA Takeaway

When a problem asks for both the best value and the number of ways to achieve it, DP states can store multiple pieces of information like maximum score and path count together.