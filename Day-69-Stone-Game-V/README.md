# Day 69 - Stone Game V

## Problem

Alice repeatedly divides a row of stones into two non-empty parts. Bob removes the part with the larger sum, while Alice adds the sum of the remaining part to her score.

If both parts have equal sums, Alice can choose which part remains.

The goal is to find the maximum score Alice can obtain before only one stone remains.

## Approach

I used **Dynamic Programming with Memoization**.

First, I calculated prefix sums so that the sum of any subarray can be found in `O(1)` time.

For every subarray `stoneValue[i...j]`, I tried every possible partition point.

For each partition:

- If the left sum is smaller, the left part remains and Alice gains the left sum.
- If the right sum is smaller, the right part remains and Alice gains the right sum.
- If both sums are equal, Alice can choose either side.

The DP state `dp(i, j)` represents the maximum score Alice can obtain from the subarray `i...j`.

## Complexity

- **Time:** O(n³)
- **Space:** O(n²)

## What I Learned

- Prefix sums make repeated subarray-sum calculations efficient.
- Interval DP is useful when a problem repeatedly divides a range into smaller ranges.
- The key is identifying the correct state and transition.
- Hard problems often become manageable once the right DP formulation is found.

## Discussion

For interval DP problems like this, do you prefer starting with recursion + memoization, or directly building a bottom-up DP?