from collections import deque

class Solution:
    def findMaxPathScore(self, edges: list[list[int]], online: list[bool], k: int) -> int:
        n = len(online)

        costs = sorted({edge[2] for edge in edges})

        if not costs:
            return -1

        def check(min_w):
            graph = [[] for _ in range(n)]
            indeg = [0] * n

            for u, v, w in edges:
                if w >= min_w and online[u] and online[v]:
                    graph[u].append((v, w))
                    indeg[v] += 1

            q = deque()

            for i in range(n):
                if indeg[i] == 0:
                    q.append(i)

            dist = [float('inf')] * n
            dist[0] = 0

            while q:
                u = q.popleft()

                for v, w in graph[u]:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w

                    indeg[v] -= 1
                    if indeg[v] == 0:
                        q.append(v)

            return dist[n - 1] <= k

        left = 0
        right = len(costs) - 1
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if check(costs[mid]):
                ans = costs[mid]
                left = mid + 1
            else:
                right = mid - 1

        return ans