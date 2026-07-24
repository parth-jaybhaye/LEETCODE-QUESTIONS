# Day 45 - Number of Unique XOR Triplets II

## Problem

In this problem, we are given an integer array and need to find the number of unique XOR values that can be formed by choosing three elements, where the indices satisfy `i ≤ j ≤ k`.

Since many different triplets can produce the same XOR value, the goal is to count only the distinct results instead of every possible triplet.

## Approach

I first removed duplicate values from the array because repeating the same value does not create any new unique XOR results.

Then, I stored all unique numbers in a set called `triplet_xors`. These represent the XOR values formed when all three selected elements are the same.

Next, I calculated the XOR of every pair of distinct numbers and stored these values in another set called `pair_xors`.

Finally, for every pair XOR, I XORed it with every unique number in the array. Each new result was added to the `triplet_xors` set. Since a set automatically removes duplicates, only unique XOR values were kept.

At the end, the size of the set gives the total number of distinct XOR triplet values.

## Time Complexity

- Time: O(m²)
- Space: O(m²)

Where:
- `m` is the number of unique values in the array.

## What I Learned

- Removing duplicate values can reduce unnecessary work.
- Sets are useful for storing only unique results.
- XOR operations can be built step by step by combining pair XORs with another number.
- Breaking a problem into smaller parts often makes the implementation much easier.