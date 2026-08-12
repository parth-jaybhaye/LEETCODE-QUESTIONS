# Day 64 - Length of Longest Subarray With at Most K Frequency

## Problem

Given an integer array `nums` and an integer `k`, find the length of the longest contiguous subarray in which the frequency of every element is at most `k`.

---

## Approach

I used the Sliding Window technique along with a hash map to keep track of the frequency of each element inside the current window.

As I expanded the right end of the window, I updated the frequency of the current element.

If adding an element caused its frequency to exceed `k`, I shrank the window from the left until the frequency became valid again.

At every step, I updated the maximum window size encountered.

---

## Time Complexity

- **Time:** O(n)
- **Space:** O(n)

---

## What I Learned

- Sliding Window is an effective approach for solving subarray problems with dynamic constraints.
- A hash map allows frequencies to be updated efficiently while expanding and shrinking the window.
- Maintaining a valid window throughout the traversal avoids checking every possible subarray, resulting in a linear-time solution.