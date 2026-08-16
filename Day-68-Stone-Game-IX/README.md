# Day 68 - Stone Game IX

## Problem

Alice and Bob take turns removing stones from a pile. Each stone has a value, and if the sum of all removed stones becomes divisible by 3 immediately after a player's move, that player loses.

If all stones are removed without anyone losing, Bob wins automatically.

The goal is to determine whether Alice can guarantee a win if both players play optimally.

## Intuition

Instead of tracking the exact values of the stones, only their remainders when divided by 3 matter because divisibility by 3 depends solely on these remainders.

Every stone belongs to one of three groups:
- Remainder 0
- Remainder 1
- Remainder 2

The parity of remainder-0 stones and the balance between remainder-1 and remainder-2 stones completely determine the outcome.

## Key Observation

There are two important cases:

- If the number of remainder-0 stones is even, Alice can win only if both remainder-1 and remainder-2 stones are available.
- If the number of remainder-0 stones is odd, the difference between the counts of remainder-1 and remainder-2 stones must be greater than 2 for Alice to force a win.

This eliminates the need for simulation or dynamic programming.

## Approach

1. Count how many stones have remainders 0, 1, and 2.
2. Check whether the count of remainder-0 stones is even or odd.
3. Apply the corresponding winning condition.
4. Return whether Alice can force a win.

## Complexity

- **Time:** O(n)
- **Space:** O(1)

## What I Learned

This was a great example of reducing a game theory problem into simple mathematical observations. By grouping stones according to their remainder modulo 3, the complex sequence of moves becomes a few concise conditions based on counts and parity.

## Discussion

When you first saw this problem, did you try simulating the game, or did you immediately think about classifying the stones by their remainders modulo 3?