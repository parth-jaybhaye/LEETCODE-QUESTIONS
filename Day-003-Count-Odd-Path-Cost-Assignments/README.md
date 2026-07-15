# Day 003 - Count Odd Path Cost Assignments

## Problem

Given a tree and multiple queries, each query asks for the number of ways to assign weights (1 or 2) to the edges on the path between two nodes so that the total path cost is odd.

The answer for every query should be returned modulo \(10^9 + 7\).

## Approach

I first represented the tree as an adjacency list.

To answer each query efficiently, I preprocessed the tree using **Binary Lifting**. A DFS is used to calculate the depth of every node and store its immediate parent. Then, a parent table is built so that the Lowest Common Ancestor (LCA) of any two nodes can be found quickly.

For each query:

- If both nodes are the same, the path contains no edges, so the answer is 0.
- Otherwise, I find the LCA of the two nodes.
- Using the node depths, I calculate the number of edges in the path.
- If the path contains `d` edges, the number of valid assignments with an odd total cost is `2^(d-1)`.
- Fast modular exponentiation is used to calculate the result efficiently.

## Complexity

- Time Complexity: **O((n + q) log n)**
- Space Complexity: **O(n log n)**

## What I Learned

- Learned how Binary Lifting helps answer LCA queries efficiently.
- Understood how preprocessing can reduce the cost of handling multiple queries.
- Improved my understanding of tree algorithms and Lowest Common Ancestor.
- Practiced combining graph traversal with mathematical observations.

## DSA Takeaway

The important part of this problem was preprocessing the tree. Once the LCA and depths of nodes were available, finding the path length became easy, and the answer could be calculated using a simple mathematical observation.