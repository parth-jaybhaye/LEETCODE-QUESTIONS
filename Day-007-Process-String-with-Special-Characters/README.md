# Day 007 - Process String with Special Characters

## Problem

Given a string containing lowercase English letters and the special characters `*`, `#`, and `%`, process the string from left to right.

The operations are:
- Letters are added to the result.
- `*` removes the last character from the result if it exists.
- `#` duplicates the current result.
- `%` reverses the current result.

Return the final string after processing all characters.

## Approach

I simulated the process by maintaining the current result.

While iterating through the string:
- If the current character is a letter, I append it to the result.
- If it is `*`, I remove the last character if the result is not empty.
- If it is `#`, I duplicate the current result.
- If it is `%`, I reverse the current result.

At the end, I join all characters to form the final string.

## Complexity

- Time Complexity: **O(n × m)** (because duplicate and reverse operations depend on the current length of the result)
- Space Complexity: **O(m)**

Where:
- `n` is the length of the input string.
- `m` is the maximum length of the generated result.

## What I Learned

- Practiced simulating operations on strings.
- Learned how different string operations affect time complexity.
- Improved my understanding of stack-like operations such as removing the last character.

## DSA Takeaway

The problem is a straightforward simulation. Carefully applying each operation in order is enough to build the correct final string.