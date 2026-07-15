# Day 016 - Count Subarrays Where Target Is Majority

## Problem

Given an array `nums` and a `target` value, count the number of subarrays in which `target` is the majority element.

A majority element is one that appears **more than half** of the total elements in the subarray.

## Approach

The key idea is to convert the problem into a prefix sum problem.

For each element:
- If it is equal to `target`, I add `+1`.
- Otherwise, I add `-1`.

For any subarray, if the sum is positive, it means the target appears more times than all other elements combined, making it the majority element.

To efficiently count previous prefix sums that satisfy this condition, I used a **Fenwick Tree (Binary Indexed Tree)**.

The Fenwick Tree stores the frequencies of prefix sums and allows prefix queries and updates in logarithmic time.

## Complexity

- Time Complexity: **O(n log n)**
- Space Complexity: **O(n)**

## What I Learned

- Learned how to transform majority problems into prefix sum problems.
- Practiced using a Fenwick Tree for efficient prefix frequency queries.
- Improved my understanding of combining prefix sums with data structures.

## DSA Takeaway

Changing the array values to `+1` and `-1` simplifies the majority condition into checking whether a subarray has a positive sum. A Fenwick Tree then makes counting such subarrays efficient.