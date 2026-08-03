# Day 55 - Stone Game III

## Problem

In this problem, Alice and Bob take turns picking 1, 2, or 3 stones from the beginning of the array. Each stone has a value, which can even be negative. Both players play optimally, and we need to determine whether Alice wins, Bob wins, or if the game ends in a tie.

## Approach

I used Dynamic Programming to keep track of the maximum score difference the current player can achieve from every position.

I created a DP array where `dp[i]` stores the maximum score difference starting from index `i`.

Starting from the end of the array, I tried taking 1, 2, and 3 stones whenever possible. For each choice, I calculated the current sum of the stones taken and subtracted the opponent's best possible score difference stored in `dp[j + 1]`.

I kept the maximum value among all valid choices.

After filling the DP array, `dp[0]` represents the final score difference if both players play optimally.

- If it is positive, Alice wins.
- If it is negative, Bob wins.
- If it is zero, the game ends in a tie.

## Time Complexity

- Time: O(n)
- Space: O(n)

## What I Learned

- Dynamic Programming can efficiently solve game strategy problems.
- Tracking the score difference is easier than calculating both players' scores separately.
- Building the DP array from the end makes the transitions straightforward.
- Trying all valid moves at each position still gives a linear-time solution because there are only three choices.