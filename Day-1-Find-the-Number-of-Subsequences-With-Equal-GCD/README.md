# Day 27 - Find the Number of Subsequences With Equal GCD

## Problem

Given an array of numbers, we need to count the number of ways to divide the elements into two subsequences such that the GCD of both subsequences is equal. The answer can be very large, so it needs to be returned using modulo `10^9 + 7`.

This problem was challenging because understanding how to keep track of all possible GCD combinations while processing the array was the main part.

## Approach

I used a dynamic programming approach with a hashmap to store different GCD states.

The idea is to process each number one by one and maintain the possible GCD values of the two subsequences.

- I used `state_counts` where each key stores a pair `(g1, g2)`, representing the current GCD of the first and second subsequence.
- Initially, both GCD values are `0` because no elements are selected.
- For every number, there are two choices:
  - Add the number to the first subsequence and update its GCD.
  - Add the number to the second subsequence and update its GCD.
- The hashmap keeps track of how many ways each `(g1, g2)` state can be reached.

The `math.gcd()` function is used to update the GCD values efficiently. At the end, I check all stored states and add the counts where both subsequences have the same non-zero GCD.

## Time Complexity

- Time: O(n * k)
- Space: O(k)

Where `n` is the length of the array and `k` is the number of different GCD states stored in the hashmap.

## What I Learned

- How to use dynamic programming with state tracking.
- How hashmaps can store and update multiple possible outcomes efficiently.
- How GCD properties can be used while building subsequences.
- This problem improved my understanding of handling complex DP states.
