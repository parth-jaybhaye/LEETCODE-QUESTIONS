# Day 021 - Find the Safest Path in a Grid

## Problem

Given an `n x n` grid where:
- `1` represents a thief.
- `0` represents an empty cell.

We need to travel from the top-left cell `(0,0)` to the bottom-right cell `(n-1,n-1)`.

The safeness factor of a path is the minimum Manhattan distance from any cell in that path to the nearest thief.

Return the maximum possible safeness factor.

## Approach

I solved this problem using **Multi-Source BFS + Binary Search**.

### Step 1: Calculate distance from thieves

I first used BFS starting from all thief cells at the same time.

This gives the minimum distance of every cell from the nearest thief.

### Step 2: Binary Search the answer

The answer represents the maximum possible safeness factor.

For a value `x`, I checked whether there exists a path where every cell has a distance of at least `x` from the thieves.

This checking is done using BFS.

If such a path exists:
- Increase the safeness value.

Otherwise:
- Decrease the safeness value.

## Complexity

- Time Complexity: **O(n² log n)**
- Space Complexity: **O(n²)**

## What I Learned

- Practiced combining BFS with Binary Search.
- Learned how multi-source BFS can calculate minimum distance from multiple starting points.
- Improved understanding of searching for the maximum possible valid answer.

## DSA Takeaway

When a problem asks for the maximum or minimum value satisfying a condition, binary search on the answer is a powerful technique. Combining it with BFS helps efficiently validate possible solutions.