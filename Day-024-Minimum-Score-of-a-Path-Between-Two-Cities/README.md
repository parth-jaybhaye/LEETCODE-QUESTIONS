# Day 024 - Minimum Score of a Path Between Two Cities

## Problem

You are given `n` cities connected by bidirectional roads.

Each road has a distance.

The score of a path is defined as the minimum distance among all roads used in that path.

Return the minimum possible score of any path from city `1` to city `n`.

## Approach

I used **Depth First Search (DFS)** to explore all cities connected to city `1`.

The important observation is:

If a city is reachable from city `1`, then every road inside that connected component can be part of some path from city `1` to city `n`.

So instead of finding a specific path, I found the minimum road distance among all roads in the connected component containing city `1`.

Steps:
1. Build an adjacency list for the graph.
2. Start DFS from city `1`.
3. Track the minimum edge distance while visiting all reachable cities.
4. Return the minimum value found.

## Complexity

- Time Complexity: **O(n + m)**
- Space Complexity: **O(n + m)**

where:
- `n` = number of cities
- `m` = number of roads

## What I Learned

- Practiced graph traversal using DFS.
- Learned that sometimes the answer depends on the entire connected component rather than a single path.
- Improved understanding of graph connectivity problems.

## DSA Takeaway

For undirected graphs, when a problem asks about paths between two nodes, checking the connected component can simplify the solution. The minimum or maximum value among all edges in that component can often determine the answer.