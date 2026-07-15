# Day 022 - Find a Safe Walk Through a Grid

## Problem

You are given a binary grid and a starting health value.

You start from the top-left cell and need to reach the bottom-right cell.

Rules:
- You can move in four directions.
- Cells with value `1` are unsafe and reduce your health by `1`.
- You can only move if your health remains positive.

Return `true` if reaching the destination is possible.

## Approach

I used **Breadth First Search (BFS)** to explore all possible paths.

During BFS, I stored three states:

- Current row
- Current column
- Remaining health

Whenever I move to a new cell:
- If the cell is unsafe, health decreases by `1`.
- If the remaining health becomes `0` or less, that path is invalid.
- Otherwise, I continue exploring.

To avoid processing the same situation repeatedly, I stored visited states using `(row, column, health)`.

If BFS reaches the destination with positive health, the answer is `true`.

## Complexity

- Time Complexity: **O(m × n × h)**
- Space Complexity: **O(m × n × h)**

where:
- `m` = number of rows
- `n` = number of columns
- `h` = possible health values

## What I Learned

- Practiced BFS with additional states.
- Learned that sometimes the same cell can be visited multiple times with different conditions.
- Understood how visited states help avoid infinite exploration.

## DSA Takeaway

In graph and grid problems, the state is not always just the position. Sometimes extra information like remaining health, cost, or distance becomes part of the state while performing BFS.