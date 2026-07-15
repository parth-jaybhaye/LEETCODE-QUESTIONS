# Day 008 - Find Kth Character After String Operations

## Problem

Given a string containing lowercase English letters and the special characters `*`, `#`, and `%`, process the string according to the given rules.

Instead of returning the entire final string, return the character at index `k`. If `k` is outside the bounds of the final string, return `'.'`.

## Approach

Building the final string directly is not possible because its length can become extremely large.

First, I calculated the length of the string after every operation without actually constructing it.

Then, I worked backwards from the end of the operations to determine where the `k`th character came from.

While moving backwards:
- For a letter, if `k` matches the position where it was added, that letter is the answer.
- For `#`, I mapped indices from the duplicated half back to the original half.
- For `%`, I reversed the index because the string was reversed.
- For `*`, only the length changes, so no index adjustment is required.

This avoids constructing the huge string while still finding the required character efficiently.

## Complexity

- Time Complexity: **O(n)**
- Space Complexity: **O(n)**

## What I Learned

- Learned how to solve problems by tracking only the string length instead of building the entire string.
- Practiced reverse simulation to recover the original position of a character.
- Improved my understanding of index mapping after string transformations.

## DSA Takeaway

Sometimes constructing the final result is unnecessary. By tracking only the length and working backwards through the operations, we can answer the query efficiently even when the final string is extremely large.