from functools import lru_cache


class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        suffix = [0] * n
        suffix[-1] = piles[-1]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @lru_cache(None)
        def dfs(i: int, M: int) -> int:
            if i + 2 * M >= n:
                return suffix[i]

            opponent = suffix[i]

            for X in range(1, 2 * M + 1):
                opponent = min(opponent, dfs(i + X, max(M, X)))

            return suffix[i] - opponent

        return dfs(0, 1)