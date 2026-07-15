# Day 001 - Maximum Total Subarray Value II

## Problem

Given an array and an integer `k`, we need to choose exactly `k` different subarrays.

The value of each subarray is calculated as:

`Maximum Element - Minimum Element`

The goal is to maximize the total value of all selected subarrays.

## Approach

This was a Hard problem.

I used a Sparse Table to quickly find the maximum and minimum element of any subarray in constant time after preprocessing.

First, I built two Sparse Tables:
- One for range maximum queries.
- One for range minimum queries.

Using these tables, I can calculate the value of any subarray efficiently.

Next, I used a priority queue (max heap). Initially, I considered the largest possible subarray starting from every index.

Each time, I selected the subarray with the highest value, added it to the answer, and then reduced its right boundary by one before inserting it back into the heap if it was still valid.

This process continues until exactly `k` subarrays are selected.

## Complexity

- Time Complexity: **O(n log n + k log n)**
- Space Complexity: **O(n log n)**

## What I Learned

- Learned how Sparse Tables answer range maximum and minimum queries efficiently.
- Understood how preprocessing can make repeated queries much faster.
- Practiced combining multiple data structures like Sparse Tables and Priority Queues in a single solution.
- Improved my understanding of solving optimization problems efficiently.

## DSA Takeaway

The main idea was to preprocess the array using Sparse Tables so that every subarray value could be calculated quickly. After that, a priority queue helped always choose the current best subarray, making the overall solution efficient.