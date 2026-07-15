# Day 020 - Number of Substrings Containing All Three Characters

## Problem

Given a string `s` containing only the characters `a`, `b`, and `c`, return the number of substrings that contain at least one occurrence of all three characters.

## Approach

I used the **sliding window** technique.

While traversing the string, I maintained the count of characters `a`, `b`, and `c` inside the current window.

Whenever the window contained all three characters:
- Every substring starting from the current left position and ending at the current right position will also be valid.
- I added the number of possible starting positions to the answer.
- Then I moved the left pointer forward to find more valid substrings.

This allows counting all valid substrings in a single traversal.

## Complexity

- Time Complexity: **O(n)**
- Space Complexity: **O(1)**

## What I Learned

- Practiced the sliding window technique.
- Learned how to count multiple valid substrings without generating them.
- Improved my understanding of maintaining character frequencies.

## DSA Takeaway

The sliding window approach is useful when we need to count subarrays or substrings that satisfy a condition. Instead of checking every substring, we maintain a valid window and count possible results efficiently.