# Day 015 - Number of ZigZag Arrays II

## Problem

Given the length of an array and a range of values, count the number of valid ZigZag arrays.

A valid ZigZag array must satisfy:
- Every element is between `l` and `r`.
- No two adjacent elements are equal.
- No three consecutive elements are strictly increasing or strictly decreasing.

Since `n` can be as large as `10^9`, the answer must be computed efficiently and returned modulo `10^9 + 7`.

## Approach

Since the array length can be extremely large, a normal Dynamic Programming solution is not fast enough.

I modeled the problem as a state transition graph. Each state represents whether the last movement was increasing or decreasing along with the last value.

A transition matrix stores all valid state changes.

Instead of applying the transitions one step at a time, I used **Matrix Exponentiation** to raise the transition matrix to the required power in logarithmic time. This efficiently computes the number of valid arrays even for very large values of `n`.

Finally, I summed all possible ending states to get the answer.

## Complexity

- Time Complexity: **O((2m)³ × log n)**
- Space Complexity: **O((2m)²)**

Where:
- `m = r - l + 1`

## What I Learned

- Learned how state transitions can be represented using matrices.
- Practiced Matrix Exponentiation for solving DP problems with very large `n`.
- Improved my understanding of logarithmic optimization techniques.

## DSA Takeaway

When a DP transition is repeated many times and `n` is very large, Matrix Exponentiation is a powerful optimization. It reduces the number of transitions from linear to logarithmic time.