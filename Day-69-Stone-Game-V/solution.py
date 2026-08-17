import math


class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)
        mem = [[-1] * n for _ in range(n)]

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        def dp(i: int, j: int) -> int:
            if i == j:
                return 0

            if mem[i][j] != -1:
                return mem[i][j]

            best = 0

            for p in range(i, j):
                left_sum = prefix[p + 1] - prefix[i]
                right_sum = prefix[j + 1] - prefix[p + 1]

                if left_sum < right_sum:
                    best = max(best, left_sum + dp(i, p))
                elif left_sum > right_sum:
                    best = max(best, right_sum + dp(p + 1, j))
                else:
                    best = max(
                        best,
                        left_sum + dp(i, p),
                        right_sum + dp(p + 1, j)
                    )

            mem[i][j] = best
            return best

        return dp(0, n - 1)