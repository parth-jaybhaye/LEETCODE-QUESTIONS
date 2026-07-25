# Day 46 - Maximum Product of Two Digits

## Problem

In this problem, we are given a positive integer. We need to find the maximum product that can be formed using any two digits from the number.

If the same digit appears more than once, it can be used multiple times as long as it exists in the number.

## Approach

I first converted the number into a list of its digits by treating it as a string. This made it easy to work with each digit separately.

Then, I sorted the list of digits in increasing order. After sorting, the last two elements are the largest digits in the number.

Finally, I multiplied these two digits and returned the result.

This approach is simple and works well because the largest product is always obtained by multiplying the two largest digits.

## Time Complexity

- Time: O(d log d)
- Space: O(d)

Where `d` is the number of digits in the integer.

## What I Learned

- How to convert an integer into a list of its digits.
- Sorting can simplify problems where we need the largest or smallest values.
- Python's string conversion makes digit extraction very easy.
- Sometimes a straightforward approach is enough to solve a problem efficiently.