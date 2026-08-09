# Day 61 - Stone Game II

## Problem

Alice and Bob play a game where they take stones from the beginning of a row of piles.

On each turn, a player can take the first `X` piles where `1 <= X <= 2M`, and `M` becomes `max(M, X)`. Both players play optimally, and the goal is to determine the maximum number of stones Alice can collect.

## Approach

I first computed a suffix sum array so I could quickly determine how many stones remain from any position.

Then I used Dynamic Programming with Memoization. The state is defined by the current index and the current value of `M`.

For every possible move, I assumed the opponent would also play optimally. Instead of directly maximizing Alice's score, I minimized the maximum score the opponent could obtain. Alice's score is simply the remaining stones minus the opponent's best possible score.

Memoization ensures that each state is solved only once.

## Time Complexity

- Time: **O(n³)**
- Space: **O(n²)**

Where:
- `n` is the number of piles.

## What I Learned

- Some game theory problems become much simpler by tracking the score difference or the opponent's best outcome instead of simulating both players separately.
- Suffix sums are very useful when the remaining total is needed repeatedly.
- Memoization over game states is an effective way to optimize recursive minimax-style solutions.