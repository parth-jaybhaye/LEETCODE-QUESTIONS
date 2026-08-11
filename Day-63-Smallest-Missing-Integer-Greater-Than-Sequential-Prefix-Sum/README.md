# Day 63 - Smallest Missing Integer Greater Than Sequential Prefix Sum

## Problem

Given an array of integers, find the longest sequential prefix where each element is exactly one greater than the previous one.

Compute the sum of this prefix, then return the smallest integer that is missing from the array and is greater than or equal to this sum.

---

## Approach

I first converted the array into a set so that checking whether a number exists could be done in constant time.

Then I traversed the array from the beginning while the numbers remained consecutive. During this traversal, I calculated the sum of the longest sequential prefix.

Finally, starting from this sum, I kept increasing the value until I found an integer that was not present in the set. That value is the required answer.

---

## Time Complexity

- **Time:** O(n)
- **Space:** O(n)

---

## What I Learned

- A hash set is an efficient choice for repeated membership checks.
- Separating the problem into finding the sequential prefix and then searching for the missing value makes the solution straightforward.
- Simple preprocessing can often eliminate the need for sorting or more complex algorithms.
```