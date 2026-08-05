# Day 57 - Remove Methods From Project

## Problem

A project contains `n` methods, and one method is known to be buggy. Any method that can be reached from this buggy method is also considered suspicious.

However, we can remove the suspicious methods only if no method outside the suspicious group calls any method inside it.

The goal is to return the remaining methods after removal, or return all methods if the removal is not valid.

## Approach

I first built a directed graph representing the method invocations.

Starting from the buggy method `k`, I performed a Breadth-First Search (BFS) to find every suspicious method that is directly or indirectly invoked. These methods were stored in a `seen` set.

Next, I checked every method that was **not** suspicious. If any of them invoked a suspicious method, then the suspicious group could not be removed, so I returned all methods.

Otherwise, every non-suspicious method was added to the answer.

## Time Complexity

- Time: O(n + m)
- Space: O(n + m)

Where:
- `n` is the number of methods.
- `m` is the number of invocations.

## What I Learned

- BFS is useful for finding all reachable nodes in a directed graph.
- Graph traversal combined with a validation step can solve dependency-related problems efficiently.
- Using a set for visited nodes makes membership checks constant time.