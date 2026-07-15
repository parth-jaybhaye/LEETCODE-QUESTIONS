# Day 011 - Maximum Building Height

## Problem

You are given the number of buildings and a set of height restrictions for some of them.

The first building must have height `0`, adjacent buildings can differ in height by at most `1`, and the restricted buildings cannot exceed their given maximum heights.

The goal is to find the maximum possible height of the tallest building.

## Approach

This was a Hard problem.

The key idea is that every restriction affects the possible heights of nearby buildings. Simply checking each restriction independently is not enough.

First, I added the mandatory restrictions for the first and last buildings and sorted all restrictions by building index.

Then I made two passes:
- A left-to-right pass to update the maximum possible height based on previous restrictions.
- A right-to-left pass to ensure the restrictions are also satisfied from the opposite direction.

After adjusting all restrictions, I checked the maximum height that could exist between every pair of consecutive restricted buildings and kept track of the largest value.

## Complexity

- Time Complexity: **O(m log m)**, where `m` is the number of restrictions.
- Space Complexity: **O(m)**

## What I Learned

- Learned how constraints can be propagated using multiple passes.
- Improved my understanding of greedy updates on sorted data.
- Practiced solving optimization problems involving ranges and restrictions.

## DSA Takeaway

The most important observation is that restrictions influence one another. By propagating constraints from both directions, we can determine the valid height range for every restricted building and then compute the maximum possible height between them.