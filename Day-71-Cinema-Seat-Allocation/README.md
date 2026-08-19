# Day 69 - Cinema Seat Allocation

## Problem

A cinema has `n` rows with 10 seats each. Some seats are already reserved.

A group of four people can sit together in one of three possible blocks:

- Seats `2, 3, 4, 5`
- Seats `4, 5, 6, 7`
- Seats `6, 7, 8, 9`

The goal is to find the maximum number of four-person groups that can be seated.

## Approach

The main challenge is that `n` can be as large as `10^9`, so we cannot process every row.

I only store rows that contain reserved seats using a dictionary-like counter.

For each affected row, I represent its reserved seats using a **bitmask**. Each bit represents whether a particular seat is reserved.

Then I check the three possible four-seat blocks using bitwise operations.

- If none of the relevant seats are reserved, the row can accommodate **2 groups**.
- If at least one valid block is available, the row can accommodate **1 group**.
- Otherwise, no group can be placed in that row.

Rows with no reserved seats can always accommodate **2 groups**, so I add:

`(n - number of affected rows) * 2`

to the final answer.

## Complexity

- **Time:** O(r)
- **Space:** O(r)

Where `r` is the number of rows containing reserved seats.

## What I Learned

- Bitmasks are extremely useful for representing a small fixed set of boolean states.
- When `n` is extremely large, processing only the affected elements can reduce the problem dramatically.
- Bitwise AND can efficiently check whether a group of seats contains any reserved seat.
- Recognizing that an empty row always supports two groups avoids unnecessary computation.

## Discussion

Would you have solved this using a set of reserved seats, or did the bitmask approach immediately come to mind?