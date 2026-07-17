# Day 38 - Sorted GCD Pair Queries

## Problem

In this problem, we are given an array of numbers and several queries. We need to consider the GCD of every possible pair of numbers, sort all those GCD values, and answer each query by returning the value at the given index in the sorted list.

Since the number of pairs can be very large, generating all pairs directly is not possible within the given constraints.

## Approach

This solution avoids checking every pair individually.

First, I counted how many numbers are divisible by each possible value. This helps identify which numbers can contribute to a particular GCD.

Then, I calculated how many pairs have each exact GCD. I started from the largest possible GCD and moved downwards. For each value, I counted all possible pairs divisible by it and removed the pairs that actually belong to larger multiples. This ensures that every pair is counted only once for its exact GCD.

After finding the number of pairs for every GCD value, I built a prefix sum array. The prefix sum tells how many pairs have GCD less than or equal to a given value.

Finally, for each query, I used binary search to quickly find the smallest GCD whose cumulative count contains that query index. This avoids constructing the entire sorted `gcdPairs` array and makes the solution efficient for large inputs.

## Time Complexity

- Time: O(M log M + N√M + Q log M)
- Space: O(M)

Where:
- `N` is the size of `nums`
- `Q` is the number of queries
- `M` is the maximum value in `nums`

## What I Learned

- How to count divisors efficiently instead of generating every pair.
- How inclusion-exclusion can be used to find the exact number of pairs for each GCD.
- How prefix sums and binary search can answer multiple queries efficiently.
- Some problems can be solved by counting frequencies instead of working with every possible combination.