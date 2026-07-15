class Solution:
    def assignEdgeWeights(self, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        MOD = 1_000_000_007
        LOG = 17

        n = len(edges) + 1
        graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        depth = [0] * (n + 1)
        parent = [[-1] * (n + 1) for _ in range(LOG)]

        def dfs(u, p):
            parent[0][u] = p
            for v in graph[u]:
                if v != p:
                    depth[v] = depth[u] + 1
                    dfs(v, u)

        import sys
        sys.setrecursionlimit(1_000_000)

        dfs(1, -1)

        for k in range(1, LOG):
            for v in range(1, n + 1):
                if parent[k - 1][v] != -1:
                    parent[k][v] = parent[k - 1][parent[k - 1][v]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != -1 and depth[parent[k][u]] >= depth[v]:
                    u = parent[k][u]

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != -1 and parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]

            return parent[0][u]

        def mod_pow(x, n):
            if n == 0:
                return 1
            if n % 2:
                return x * mod_pow(x % MOD, n - 1) % MOD
            return mod_pow(x * x % MOD, n // 2) % MOD

        ans = []

        for u, v in queries:
            if u == v:
                ans.append(0)
            else:
                a = lca(u, v)
                d = depth[u] + depth[v] - 2 * depth[a]
                ans.append(mod_pow(2, d - 1))

        return ans