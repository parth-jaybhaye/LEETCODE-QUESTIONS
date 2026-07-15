# Day 012 - Maximum Ice Cream Bars

## Problem

Given the cost of each ice cream bar and a limited number of coins, find the maximum number of ice cream bars that can be purchased.

The order of buying does not matter.

## Approach

I used a greedy approach.

Since every ice cream bar contributes equally to the final count, it is always better to buy the cheapest bars first. I sorted the costs array in ascending order and started purchasing bars one by one.

As long as I had enough coins, I bought the current bar and reduced the remaining coins. Once I couldn't afford the next bar, I returned the number of bars purchased.

## Complexity

- Time Complexity: **O(n log n)**
- Space Complexity: **O(1)** (excluding the space used by sorting)

## What I Learned

- Learned how greedy algorithms help maximize the number of items.
- Practiced identifying when sorting leads to an optimal solution.
- Improved my understanding of optimization problems involving limited resources.

## DSA Takeaway

The key observation is that every ice cream bar has the same value in terms of the final answer—it always increases the count by one. Therefore, buying the cheapest bars first is the optimal greedy strategy.