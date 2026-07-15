# Day 2 - GCD of Odd and Even Sums

## Problem

In this problem, we are given an integer `n`. We need to find the GCD of two values:
- The sum of the first `n` odd numbers.
- The sum of the first `n` even numbers.

Instead of calculating both sums directly, the goal is to find the result in the simplest way possible.

## Approach

At first, it looks like we need to calculate both sums and then find their GCD. But after observing the pattern, we can use a mathematical property.

- The sum of the first `n` odd numbers is `n²`.
- The sum of the first `n` even numbers is `n × (n + 1)`.

Now we need to find the GCD of `n²` and `n(n + 1)`. Since `n` and `n + 1` are always coprime, the answer is simply `n`.

Because of this observation, the solution only needs to return `n` without performing any extra calculations.

## Time Complexity

- Time: O(1)
- Space: O(1)

## What I Learned

- Looking for mathematical patterns can make a problem much simpler.
- The sum of the first `n` odd numbers is `n²`.
- The sum of the first `n` even numbers is `n(n + 1)`.
- Understanding number theory can sometimes reduce a problem to a one-line solution.