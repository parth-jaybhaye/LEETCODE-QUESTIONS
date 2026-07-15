# Day 010 - Find the Highest Altitude

## Problem

A biker starts at altitude `0` and travels through different points. The `gain` array represents the change in altitude between consecutive points.

The task is to find the highest altitude reached during the journey.

## Approach

I used a running sum (prefix sum) approach.

Starting from altitude `0`, I kept adding each value from the `gain` array to get the current altitude. After every update, I compared the current altitude with the highest altitude found so far and updated the answer if needed.

Since the altitude is calculated only once for each point, a single traversal is enough.

## Complexity

- Time Complexity: **O(n)**
- Space Complexity: **O(1)**

## What I Learned

- Practiced using the prefix sum technique.
- Learned how maintaining a running total can solve array problems efficiently.
- Improved my understanding of tracking the maximum value during traversal.

## DSA Takeaway

This problem is a good example of the prefix sum technique. Instead of storing every altitude, we only need to maintain the current altitude and the maximum altitude reached so far.