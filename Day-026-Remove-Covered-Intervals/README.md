# Day 026 - Remove Covered Intervals

## Problem Statement

Given an array of intervals where `intervals[i] = [li, ri)` represents the interval `[li, ri)`, remove all intervals that are covered by another interval.

An interval `[a, b)` is covered by `[c, d)` if:

- `c <= a`
- `b <= d`

Return the number of intervals remaining after removing all covered intervals.

---

## Approach

To solve this problem, we use sorting and a greedy approach.

Steps:

1. Sort the intervals:
   - Sort by starting point in increasing order.
   - If two intervals have the same starting point, sort by ending point in decreasing order.

2. Traverse the sorted intervals while maintaining the maximum ending point seen so far.

3. If the current interval's ending point is less than or equal to the maximum ending point, then it is covered by a previous interval.

4. Otherwise, update the maximum ending point and count the interval as a remaining interval.

---

## Example

### Input

```
intervals = [[1,4],[3,6],[2,8]]
```

### Explanation

After sorting:

```
[[1,4],[2,8],[3,6]]
```

- `[1,4]` is not covered, so we keep it.
- `[2,8]` extends the maximum range, so we keep it.
- `[3,6]` is covered by `[2,8]`, so we remove it.

### Output

```
2
```

---

## Complexity Analysis

- Time Complexity: `O(n log n)`
  - Sorting the intervals takes `O(n log n)` time.

- Space Complexity: `O(1)`
  - Only constant extra space is used excluding sorting space.

---

## What I Learned

This problem helped me understand how sorting can simplify interval problems.

Instead of comparing every pair of intervals, which would take `O(n²)`, sorting allows us to solve the problem efficiently using a single traversal.

The main idea is that once intervals are sorted properly, we only need to track the maximum ending point to identify covered intervals.

---

## Topics

- Sorting
- Greedy Algorithm
- Intervals