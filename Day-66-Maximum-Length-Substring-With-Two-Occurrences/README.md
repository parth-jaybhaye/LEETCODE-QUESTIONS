# Day 66 - Maximum Length Substring With Two Occurrences

## Problem

Given a string `s`, find the maximum length of a substring in which every character appears at most two times.

## Approach

I used the **Sliding Window** technique to efficiently maintain a valid substring.

Two pointers (`l` and `r`) define the current window, while a frequency map stores the count of each character inside the window.

As the right pointer expands the window, the frequency of the current character is increased. If any character appears more than twice, the left pointer moves forward, decreasing frequencies until the window becomes valid again.

Throughout the traversal, I keep track of the maximum window length.

## Time Complexity

- Time: **O(n)**
- Space: **O(1)**

Where:

- `n` is the length of the string.
- The frequency map stores at most 26 lowercase English letters.

## What I Learned

- Sliding Window is one of the most effective techniques for substring problems with frequency constraints.
- Maintaining character frequencies allows efficient validation of the current window.
- Expanding and shrinking the window dynamically leads to a linear-time solution.