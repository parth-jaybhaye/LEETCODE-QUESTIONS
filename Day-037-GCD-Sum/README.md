# Day 38 - GCD Sum

## Problem

In this problem, we are given an array of integers. First, we need to create a new array where each element is the GCD of the current number and the maximum value seen so far. After that, the new array is sorted. Then, the smallest and largest elements are paired together, and the GCD of each pair is added to the final answer. If one element is left in the middle, it is ignored.

## Approach

I created a custom GCD function using the Euclidean algorithm instead of using the built-in `math.gcd()`.

First, I traversed the array while keeping track of the maximum value seen so far. For every element, I calculated the GCD of the current number and the current maximum, then stored it in a new array called `prefixGcd`.

After building the array, I sorted it in increasing order.

To form the required pairs, I used two pointers. One pointer started from the beginning of the sorted array, and the other started from the end. For each pair, I calculated their GCD and added it to the answer. Then I moved both pointers towards the center until all possible pairs were processed.

## Time Complexity

- Time: O(n log n)
- Space: O(n)

## What I Learned

- How to implement the Euclidean algorithm to find the GCD.
- How to build a new array while keeping track of a running maximum.
- Using sorting and the two-pointer technique to form pairs efficiently.
- Breaking the solution into small steps makes the implementation easier to understand.