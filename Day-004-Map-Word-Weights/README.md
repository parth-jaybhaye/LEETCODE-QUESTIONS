# Day 004 - Map Word Weights

## Problem

Given a list of words and the weights of each lowercase English letter, calculate the weight of every word.

For each word:
- Find the sum of the weights of all its characters.
- Take the result modulo 26.
- Convert the value into a character using reverse alphabetical order:
  - 0 → 'z'
  - 1 → 'y'
  - ...
  - 25 → 'a'

Return the final string formed by joining all the mapped characters.

## Approach

I processed each word one by one.

For every character in the word, I added its corresponding weight from the given array. After calculating the total weight of the word, I took it modulo 26.

Finally, I converted the result into the required character using the reverse alphabetical mapping and appended it to the answer string.

## Complexity

- Time Complexity: **O(n × m)**
  - `n` is the number of words.
  - `m` is the average length of each word.
- Space Complexity: **O(1)** (excluding the output string).

## What I Learned

- Practiced working with character-to-index conversion using ASCII values.
- Learned how modulo operations can be combined with custom mappings.
- Improved my understanding of string processing and simulation problems.

## DSA Takeaway

This problem mainly tests careful implementation. Breaking it into small steps—calculating the word weight, applying modulo, and mapping the result—makes the solution straightforward.