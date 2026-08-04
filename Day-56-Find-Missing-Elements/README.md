# Day 56 - Find Missing Elements

## Problem

In this problem, we are given an array of unique integers. The smallest and largest numbers belong to the original range, but some numbers between them may be missing.

The task is to return all the missing numbers in sorted order.

## Approach

I first found the smallest and largest values in the array because they define the complete range.

Then, I stored all the elements in a set. Using a set makes checking whether a number exists very fast.

After that, I iterated through every number between the minimum and maximum values. If a number was not present in the set, I added it to the answer list.

Finally, I returned the list of all missing numbers.

Using a set keeps the solution simple and efficient.

## Time Complexity

- Time: O(n + r)
- Space: O(n)

Where:
- `n` is the size of the input array.
- `r` is the size of the range between the minimum and maximum values.

## What I Learned

- Sets provide fast membership checking.
- Finding the minimum and maximum values helps define the search range.
- List comprehensions can make code shorter and easier to read.
- Simple data structures are often enough for easy problems.