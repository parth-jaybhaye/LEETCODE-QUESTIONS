# Day 023 - Maximum Path Score in a DAG

## Problem

You are given a directed acyclic graph (DAG).

Each edge has:
- A recovery cost.
- A score value.

Some nodes may be offline and cannot be used in a path.

A valid path:
- Starts from node `0`.
- Ends at node `n - 1`.
- Uses only online nodes.
- Has total edge cost less than or equal to `k`.

The score of a path is the minimum edge cost present in that path.

Return the maximum possible score among all valid paths.

## Approach

I used **Binary Search on Answer + Topological Sort**.

### Step 1: Binary Search

The answer represents the minimum edge weight that a valid path can maintain.

For a chosen minimum weight:
- I removed all edges having smaller costs.
- Then I checked if a valid path still exists.

If a path exists:
- The score can be increased.

Otherwise:
- The score needs to be reduced.

### Step 2: Checking a value

For each binary search step:
- I created a filtered DAG containing only valid edges.
- Used topological sorting to process nodes.
- Applied dynamic programming to find the minimum total cost from node `0` to every node.

If the cost to reach the destination is within `k`, the chosen score is possible.

## Complexity

- Time Complexity: **O((n + m) log m)**
- Space Complexity: **O(n + m)**

where:
- `n` = number of nodes
- `m` = number of edges

## What I Learned

- Practiced binary search on answer problems.
- Learned how DAG shortest paths can be solved using topological order.
- Improved understanding of combining multiple algorithms for optimization problems.

## DSA Takeaway

When a problem asks for the maximum value satisfying a condition, binary search can reduce the search space. If checking a value is efficient, the overall solution becomes much faster.