# Day 017 - Count Subarrays Where Target Is Majority II

## Problem

Given an array `nums` and an integer `target`, count the number of subarrays where `target` is the majority element.

A majority element is one that appears **more than half** the number of times in the subarray.

## Approach

I transformed the array into a prefix sum problem.

For each element:
- If it is equal to `target`, I added `+1`.
- Otherwise, I added `-1`.

With this transformation, any subarray having a positive sum means the target appears more times than all the other elements combined, making it the majority.

To efficiently count such subarrays, I maintained the frequencies of prefix sums using a **Fenwick Tree (Binary Indexed Tree)**.

For every new prefix sum:
- I queried how many previous prefix sums were smaller than the current one.
- Then I updated the Fenwick Tree with the current prefix sum.

This avoids checking every subarray individually and keeps the solution efficient for large inputs.

## Complexity

- Time Complexity: **O(n log n)**
- Space Complexity: **O(n)**

## What I Learned

- Practiced converting majority conditions into prefix sum comparisons.
- Learned how Fenwick Trees can efficiently maintain prefix frequencies.
- Improved my understanding of prefix-sum-based counting techniques.

## DSA Takeaway

Instead of checking every subarray, transforming the problem into prefix sums allows us to count valid subarrays efficiently. A Fenwick Tree helps perform the required updates and queries in logarithmic time.