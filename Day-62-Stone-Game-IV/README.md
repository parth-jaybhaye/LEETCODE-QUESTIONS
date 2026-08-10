# Day 62 - Stone Game IV

## Problem

Alice and Bob take turns removing a perfect square number of stones from a pile containing `n` stones.

Both players play optimally, and the player who cannot make a move loses.

The goal is to determine whether Alice, who moves first, can guarantee a win.

---

## Approach

I used Dynamic Programming where `dp[i]` represents whether the current player can force a win with `i` stones remaining.

Starting from `1` up to `n`, I checked every perfect square that could be removed. If removing a perfect square leaves the opponent in a losing state, then the current state is marked as winning.

The answer is simply the value of `dp[n]`.

---

## Time Complexity

- **Time:** O(n√n)
- **Space:** O(n)

---

## What I Learned

- Dynamic Programming works well for turn-based game problems by representing winning and losing states.
- A state is winning if there exists at least one move that forces the opponent into a losing state.
- Checking all possible perfect square moves efficiently solves the problem within the given constraints.