# Day 006 - Delete the Middle Node of a Linked List

## Problem

Given the head of a linked list, delete its middle node and return the head of the modified list.

If the list contains only one node, return an empty list.

## Approach

I used the fast and slow pointer technique to find the middle node.

The slow pointer moves one step at a time, while the fast pointer moves two steps. At the same time, I kept track of the node just before the slow pointer.

When the fast pointer reaches the end of the list, the slow pointer points to the middle node. I then removed the middle node by connecting the previous node directly to the next node.

## Complexity

- Time Complexity: **O(n)**
- Space Complexity: **O(1)**

## What I Learned

- Practiced using the fast and slow pointer technique on linked lists.
- Learned how to delete a node without traversing the list multiple times.
- Improved my understanding of pointer manipulation in linked lists.

## DSA Takeaway

The fast and slow pointer approach is a simple and efficient way to locate the middle of a linked list. Keeping track of the previous node allows the middle node to be removed in a single traversal.