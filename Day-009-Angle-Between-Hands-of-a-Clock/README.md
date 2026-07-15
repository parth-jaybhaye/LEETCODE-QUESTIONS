# Day 009 - Angle Between Hands of a Clock

## Problem

Given the current hour and minutes on a clock, find the smaller angle formed between the hour hand and the minute hand.

## Approach

First, I calculated the position of both clock hands.

- The minute hand moves **6° per minute**.
- The hour hand moves **30° per hour**, but it also moves **0.5° every minute** as time passes.

After calculating both angles, I found the absolute difference between them. Since there are always two angles between the hands, I returned the smaller one.

## Complexity

- Time Complexity: **O(1)**
- Space Complexity: **O(1)**

## What I Learned

- Learned how to convert time into angles.
- Understood that the hour hand moves continuously, not just every hour.
- Practiced solving a simple math-based simulation problem.

## DSA Takeaway

This problem is based on mathematical observation rather than data structures. Carefully calculating the position of each hand is enough to find the required angle.