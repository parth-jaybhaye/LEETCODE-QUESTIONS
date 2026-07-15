# Day 002 - Assign Edge Weights

## Problem

Given a tree rooted at node 1, every edge must be assigned a weight of either 1 or 2.

Choose any node at the maximum depth and consider only the path from the root to that node. The task is to count the number of ways to assign weights so that the total cost of this path is odd.

Since the answer can be very large, return it modulo \(10^9 + 7\).

## Approach

The first step is to find the maximum depth of the tree. I used Breadth-First Search (BFS) starting from node 1 to calculate the number of levels in the tree.

If the longest path contains `L` edges, then every edge can have either weight 1 or 2. This gives a total of `2^L` possible assignments.

To make the total path cost odd, exactly half of these assignments are valid because changing the parity of one edge changes the parity of the total sum.

Therefore, the final answer becomes:

- If the path contains at least one edge, the answer is `2^(L-1)`.
- The implementation computes this efficiently using fast modular exponentiation.

## Complexity

- Time Complexity: **O(n)**
- Space Complexity: **O(n)**

## What I Learned

- Learned how BFS can be used to find the maximum depth of a tree.
- Understood how parity (odd and even) can simplify counting problems.
- Practiced using fast exponentiation to compute large powers under modulo.
- Improved my understanding of combining graph traversal with mathematical observations.

## DSA Takeaway

The important part of this problem was realizing that we only need the depth of the deepest path. After finding it using BFS, the answer follows from a simple parity observation and can be calculated efficiently using modular exponentiation.