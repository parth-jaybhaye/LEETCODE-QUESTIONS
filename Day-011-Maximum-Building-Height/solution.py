class Solution(object):
    def maxBuilding(self, n, restrictions):
        restrictions.append([1, 0])

        found = False
        for r in restrictions:
            if r[0] == n:
                found = True
                break

        if not found:
            restrictions.append([n, n - 1])

        restrictions.sort()

        m = len(restrictions)

        for i in range(1, m):
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i - 1][1] + restrictions[i][0] - restrictions[i - 1][0]
            )

        for i in range(m - 2, -1, -1):
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i + 1][1] + restrictions[i + 1][0] - restrictions[i][0]
            )

        ans = 0

        for i in range(1, m):
            x1, h1 = restrictions[i - 1]
            x2, h2 = restrictions[i]

            ans = max(ans, (h1 + h2 + x2 - x1) // 2)

        return ans