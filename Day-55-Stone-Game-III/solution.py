import math


class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        dp = [-math.inf] * n + [0]

        for i in reversed(range(n)):
            curr_sum = 0
            for j in range(i, min(i + 3, n)):
                curr_sum += stoneValue[j]
                dp[i] = max(dp[i], curr_sum - dp[j + 1])

        score = dp[0]

        if score == 0:
            return "Tie"

        return "Alice" if score > 0 else "Bob"