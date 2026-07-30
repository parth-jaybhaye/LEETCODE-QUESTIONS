## Problem

In this problem, we are given a word with distinct lowercase letters. We can remap the letters to the phone keypad in any way we want. The goal is to minimize the total number of key presses needed to type the word.

Since there are only 8 keys available (2 to 9), we need to assign letters carefully so that the total cost is as small as possible.

## Approach

I first counted the frequency of each character using `Counter`. Although every character appears only once in this version of the problem, using frequencies keeps the solution simple and also works well for similar problems.

Then, I sorted the frequencies in descending order.

The first 8 characters can be placed in the first position of the keys, so they require only one push each. The next 8 characters require two pushes, the next 8 require three pushes, and so on.

For each frequency, I calculated its cost using `i // 8 + 1`, where `i` is its position after sorting. Finally, I multiplied the frequency by its required number of pushes and added everything to get the answer.

## Time Complexity

- Time: O(n log n)
- Space: O(n)

Where `n` is the number of distinct characters in the word.

## What I Learned

- Greedy assignment helps minimize the total number of key presses.
- Sorting frequencies ensures the most important characters get the lowest cost.
- Integer division can be used to determine the push count for each group of 8 characters.
- A solution can be written in a very compact way by combining sorting and enumeration.