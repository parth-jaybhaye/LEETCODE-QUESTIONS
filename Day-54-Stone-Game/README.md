# Day 54 - Stone Game

## Problem

In this problem, Alice and Bob take turns picking a pile of stones from either end of the row. Both players play optimally, and we need to determine whether Alice can always win the game.

Instead of simulating every possible game, we need to find the best strategy for both players.

## Approach

I used Dynamic Programming to keep track of the maximum score difference the current player can achieve over the opponent.

I created a 1D DP array where each value represents the best score difference for a particular subarray.

For every subarray, the current player has two choices:

- Take the left pile.
- Take the right pile.

If the current player takes the left pile, the opponent will play optimally on the remaining piles. The same idea applies when taking the right pile.

So, for every range, I chose the option that gives the maximum score difference.

After processing all subarrays, if the final score difference is positive, Alice can collect more stones than Bob, so the answer is `True`.

Using a 1D DP array helps reduce the memory needed compared to a full 2D DP table.

## Time Complexity

- Time: O(n²)
- Space: O(n)

## What I Learned

- Many game problems can be solved by tracking the score difference instead of the actual scores.
- Dynamic Programming can efficiently solve optimal game strategy problems.
- A 2D DP solution can often be optimized into a 1D DP array.
- Updating DP values in the correct order is important when using space optimization.