# Day 005 - Maximum Twin Sum of a Linked List

## Problem

Given an even-length linked list, every node has a twin. The twin of the `i-th` node is the `(n-1-i)-th` node.

The twin sum is the sum of a node and its twin. The task is to find the maximum twin sum among all pairs.

## Approach

I used the fast and slow pointer technique to find the middle of the linked list.

After finding the middle, I reversed the second half of the list. This allowed me to compare the first half and the reversed second half node by node.

For each pair, I calculated the twin sum and kept track of the maximum value.

## Complexity

- Time Complexity: **O(n)**
- Space Complexity: **O(1)**

## What I Learned

- Practiced using fast and slow pointers to find the middle of a linked list.
- Learned how reversing the second half of a linked list helps compare symmetric nodes.
- Improved my understanding of in-place linked list manipulation.

## DSA Takeaway

This problem combines multiple linked list techniques in one solution. Finding the middle, reversing the second half, and comparing both halves together leads to an efficient O(n) solution without using extra space.