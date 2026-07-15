class Solution:
    def minScore(self, n, roads):
        graph = [[] for _ in range(n + 1)]

        for a, b, d in roads:
            graph[a].append((b, d))
            graph[b].append((a, d))

        visited = [False] * (n + 1)
        ans = float('inf')

        def dfs(node):
            nonlocal ans

            visited[node] = True

            for nxt, dist in graph[node]:
                ans = min(ans, dist)

                if not visited[nxt]:
                    dfs(nxt)

        dfs(1)

        return ans