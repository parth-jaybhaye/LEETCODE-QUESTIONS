# Day 014 - Number of ZigZag Arrays I

## Problem

Given the length of an array and a range of values, count the number of valid ZigZag arrays.

A valid ZigZag array must satisfy:
- Every element is between `l` and `r`.
- No two adjacent elements are equal.
- No three consecutive elements are strictly increasing or strictly decreasing.

Return the total number of valid arrays modulo `10^9 + 7`.

## Approach

This problem can be solved using Dynamic Programming.

For every possible ending value, I maintained two DP states:
- `up`: the previous comparison was increasing.
- `down`: the previous comparison was decreasing.

For each new position, I used prefix sums to efficiently calculate how many previous states could transition into the current value without violating the ZigZag conditions.

Instead of checking every previous value one by one, prefix sums allow each transition to be computed in constant time, making the overall solution efficient.

## Complexity

- Time Complexity: **O(n × m)**
- Space Complexity: **O(m)**

Where:
- `n` is the length of the array.
- `m = r - l + 1` is the number of possible values.

## What I Learned

- Practiced Dynamic Programming with multiple states.
- Learned how prefix sums can optimize DP transitions.
- Improved my understanding of sequence-based DP problems.

## DSA Takeaway

A direct DP solution would be too slow because every state depends on many previous values. Using prefix sums reduces the transition time significantly, making the solution efficient enough for the given constraints.