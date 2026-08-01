# Day 53 - Predict the Winner

## Problem

In this problem, two players take turns picking a number from either the beginning or the end of the array. Both players play optimally, and we need to determine whether Player 1 can end the game with a score greater than or equal to Player 2.

## Approach

Instead of calculating the actual scores of both players, I focused on the score difference between the current player and the opponent.

I used a 1D dynamic programming array where `dp[i]` stores the maximum score difference the current player can achieve for a particular subarray.

For every subarray, there are two choices:

- Pick the left number and subtract the opponent's best possible score difference.
- Pick the right number and subtract the opponent's best possible score difference.

I chose the option that gives the maximum score difference.

At the end, if the score difference for the entire array is greater than or equal to zero, Player 1 can win or tie the game, so I return `True`.

Using a 1D DP array instead of a 2D table helps reduce the space complexity while keeping the same logic.

## Time Complexity

- Time: O(n²)
- Space: O(n)

## What I Learned

- Some game problems can be solved by tracking score differences instead of actual scores.
- Dynamic Programming can optimize recursive game strategies.
- A 2D DP solution can sometimes be reduced to a 1D DP array.
- Thinking in terms of the opponent's best move simplifies many game theory problems.