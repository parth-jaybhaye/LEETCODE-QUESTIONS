# Day 68 - Find the Largest Almost Missing Integer

## Problem

An integer is considered **almost missing** if it appears in exactly one subarray of size `k`.

The goal is to find the largest almost missing integer. If no such integer exists, return `-1`.

## Approach

The key observation is that an element can appear in exactly one subarray of size `k` only in specific positions.

First, I handled the case where `k` equals the length of the array. In this case, there is only one subarray, so the largest element is the answer.

For `k = 1`, every element forms its own subarray. Therefore, an integer is almost missing only when it occurs exactly once in the entire array.

For `k > 1`, only the first and last elements can appear in exactly one subarray:

- `nums[0]` belongs only to the first subarray.
- `nums[-1]` belongs only to the last subarray.

So I count the frequency of every number and check whether the first or last element occurs exactly once. The larger valid value is returned.

## Complexity

- **Time:** O(n)
- **Space:** O(n)

## What I Learned

- Sometimes the key to an array problem is understanding how elements participate in subarrays rather than generating every subarray.
- Boundary elements have special properties because they belong to fewer subarrays.
- Handling special cases like `k = 1` and `k = n` can simplify the main logic significantly.

## Discussion

Did you first try generating all subarrays, or did you notice that only the boundary elements can be almost missing when `k > 1`?