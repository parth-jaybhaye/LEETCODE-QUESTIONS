# Day 028 - Sum and Multiply Queries

## Problem Statement

You are given a string `s` consisting of digits and a list of queries.

For each query `[l, r]`:

1. Extract the substring `s[l..r]`.
2. Create a number `x` by concatenating all non-zero digits in the substring.
3. Calculate the sum of digits of `x`.
4. Return:

```
x * sum
```

All answers must be returned modulo `10^9 + 7`.

---

## Approach

For each query, we need to extract non-zero digits and calculate their value.

Steps:

1. Traverse the substring from `l` to `r`.
2. Ignore zero digits.
3. Build the number `x` by appending non-zero digits.
4. Maintain the sum of these digits.
5. Return `(x * sum) % MOD`.

---

## Example

### Input

```
s = "10203004"
queries = [[0,7],[1,3],[4,6]]
```

### Processing

Query `[0,7]`:

```
Substring = "10203004"

Non-zero digits = 1234

Sum = 1+2+3+4 = 10

Answer = 1234 * 10 = 12340
```

Query `[1,3]`:

```
Substring = "020"

x = 2

sum = 2

Answer = 4
```

### Output

```
[12340,4,9]
```

---

## Complexity Analysis

- Time Complexity: `O(n + q*n)`
  - `n` is the length of the string.
  - `q` is the number of queries.

- Space Complexity: `O(n)`

---

## What I Learned

This problem focuses on handling digit manipulation inside multiple ranges.

The main challenge is preserving the order of non-zero digits while calculating the resulting number.

Using prefix information can help optimize repeated queries by avoiding unnecessary recalculation.

---

## Topics

- String Manipulation
- Prefix Processing
- Mathematics
- Modular Arithmetic