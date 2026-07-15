# Day 013 - Maximum Number of Balloons

## Problem

Given a string `text`, determine the maximum number of times the word **"balloon"** can be formed using its characters.

Each character in the string can be used at most once.

## Approach

I counted the frequency of every character in the given string.

The word **"balloon"** requires:
- `b` → 1 time
- `a` → 1 time
- `l` → 2 times
- `o` → 2 times
- `n` → 1 time

So, after counting the characters, I divided the counts of `l` and `o` by 2 because they appear twice in the target word.

Finally, I returned the minimum among the required character counts, as the least available character determines how many complete words can be formed.

## Complexity

- Time Complexity: **O(n)**
- Space Complexity: **O(1)**

## What I Learned

- Practiced using frequency counting to solve string problems.
- Learned how repeated characters affect the final answer.
- Improved my understanding of counting-based approaches.

## DSA Takeaway

Many string problems become simple after counting character frequencies. The limiting character determines the maximum number of valid words that can be formed.