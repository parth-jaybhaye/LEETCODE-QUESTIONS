# Day 41 - Shift 2D Grid

## Problem

In this problem, we are given a 2D grid and an integer `k`. We need to shift every element to the right `k` times. When an element reaches the end of a row, it moves to the beginning of the next row. The last element of the grid wraps around to the first position.

The goal is to return the grid after performing all the shifts.

## Approach

Instead of shifting the grid one step at a time, I calculated the final position of each element directly.

First, I found the total number of elements in the grid and reduced `k` using the modulo operator. This avoids doing unnecessary shifts when `k` is larger than the total number of elements.

Then, I created a new grid of the same size to store the answer.

For each element, I converted its row and column into a single index. After adding `k` to this index, I used modulo again to keep the index inside the valid range.

Finally, I converted the new index back into row and column values and placed the element in its correct position in the result grid.

This approach shifts all elements in one traversal without repeating the operation multiple times.

## Time Complexity

- Time: O(m × n)
- Space: O(m × n)

Where:
- `m` is the number of rows.
- `n` is the number of columns.

## What I Learned

- How to convert between 2D coordinates and a 1D index.
- Using modulo helps handle circular shifts efficiently.
- Computing the final position directly is much better than performing one shift at a time.
- Creating a separate result grid makes the implementation simple and easy to understand.