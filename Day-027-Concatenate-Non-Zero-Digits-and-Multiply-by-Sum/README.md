# Day 027 - Concatenate Non-Zero Digits and Multiply by Sum

## Problem Statement

You are given an integer `n`.

Create a new integer `x` by concatenating all the non-zero digits of `n` in their original order.

If there are no non-zero digits, `x = 0`.

Let `sum` be the sum of digits in `x`.

Return the value of:

```
x * sum
```

---

## Approach

The problem can be solved by processing the digits of `n`.

Steps:

1. Convert the number into a string to easily access each digit.
2. Traverse each digit:
   - Ignore all zero digits.
   - Store non-zero digits to build `x`.
   - Add each non-zero digit to calculate the digit sum.
3. Convert the collected digits into an integer.
4. Return `x * sum`.

---

## Example

### Input

```
n = 10203004
```

### Processing

Non-zero digits:

```
1, 2, 3, 4
```

So:

```
x = 1234
sum = 1 + 2 + 3 + 4 = 10
```

Result:

```
1234 * 10 = 12340
```

### Output

```
12340
```

---

## Complexity Analysis

- Time Complexity: `O(log n)`
  - We process each digit of the number once.

- Space Complexity: `O(log n)`
  - Extra space is used to store the non-zero digits.

---

## What I Learned

This problem demonstrates simple digit manipulation techniques.

Converting the number into a string makes it easier to preserve the original order of digits while filtering out unwanted values.

The key observation is that we only need to keep track of non-zero digits and their sum.

---

## Topics

- String Manipulation
- Mathematics
- Simulation