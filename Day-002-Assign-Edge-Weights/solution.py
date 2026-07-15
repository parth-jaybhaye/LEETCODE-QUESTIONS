from collections import deque

class Solution:
    def assignEdgeWeights(self, edges: list[list[int]]) -> int:
        MOD = 1_000_000_007

        n = len(edges) + 1
        graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        q = deque([1])
        seen = [False] * (n + 1)
        seen[1] = True

        step = 0

        while q:
            for _ in range(len(q)):
                u = q.popleft()

                for v in graph[u]:
                    if not seen[v]:
                        seen[v] = True
                        q.append(v)

            step += 1

        return self.mod_pow(2, step - 2, MOD) if step > 0 else 0

    def mod_pow(self, x: int, n: int, mod: int) -> int:
        if n == 0:
            return 1

        if n % 2 == 1:
            return (x * self.mod_pow(x % mod, n - 1, mod)) % mod

        return self.mod_pow((x * x) % mod, n // 2, mod)