# Day 019 - Number of Strings That Appear as Substrings in Word

## Problem

Given an array of strings `patterns` and a string `word`, count how many strings from `patterns` appear as a substring inside `word`.

A substring is a continuous sequence of characters within a string.

## Approach

I checked each pattern one by one and used substring searching to determine whether it exists inside `word`.

If a pattern is found in `word`, I incremented the count.

Since the input size is small, a direct simulation approach is sufficient.

## Complexity

- Time Complexity: **O(n × m × k)**
  - `n` = number of patterns
  - `m` = length of each pattern
  - `k` = length of word
- Space Complexity: **O(1)**

## What I Learned

- Practiced string searching operations.
- Learned how simple built-in substring checking can solve small constraint problems.
- Improved my understanding of handling multiple string comparisons.

## DSA Takeaway

Not every string problem requires advanced algorithms. When constraints are small, a simple and clear approach is often the most efficient and readable solution.