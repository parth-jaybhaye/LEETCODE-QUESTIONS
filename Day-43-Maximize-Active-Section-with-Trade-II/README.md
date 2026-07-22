# Day 43 - Maximize Active Section with Trade II

## Problem

In this problem, we are given a binary string and multiple queries. For each query, we need to consider only the given substring and perform at most one trade to maximize the number of active sections.

Unlike the previous version of the problem, we now have many queries, so solving each one from scratch would be too slow.

## Approach

This solution first preprocesses the string by finding every continuous group of `0`s. It stores the starting position and length of each group so they can be accessed quickly later.

To answer queries efficiently, I used two Sparse Tables.

- The first Sparse Table stores the maximum size of a single zero group in any range.
- The second Sparse Table stores the maximum combined length of two adjacent zero groups. This helps when a trade can merge two groups into a larger active section.

For each query, I determine which zero groups are completely or partially inside the substring. Then I check different possible cases, such as using a partial group, a complete group, or merging two neighboring groups. The maximum gain from these cases is added to the number of active sections already present in the original string.

Using preprocessing and range maximum queries allows every query to be answered much faster than rebuilding the answer each time.

## Time Complexity

- Preprocessing: O(n log n)
- Each Query: O(1)
- Overall: O(n log n + q)

Where:
- `n` is the length of the string.
- `q` is the number of queries.

## What I Learned

- How preprocessing can make multiple queries much faster.
- How Sparse Tables can answer range maximum queries in constant time.
- How grouping consecutive elements simplifies interval-based problems.
- Breaking a hard problem into preprocessing and query handling makes the solution easier to manage.