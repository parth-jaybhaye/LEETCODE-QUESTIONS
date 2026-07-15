class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        import heapq

        n = len(nums)

        lg = [0] * (n + 1)
        for i in range(2, n + 1):
            lg[i] = lg[i // 2] + 1

        LOG = lg[n] + 1

        mx = [[0] * n for _ in range(LOG)]
        mn = [[0] * n for _ in range(LOG)]

        for i in range(n):
            mx[0][i] = nums[i]
            mn[0][i] = nums[i]

        for j in range(1, LOG):
            length = 1 << j
            half = 1 << (j - 1)

            for i in range(n - length + 1):
                mx[j][i] = max(mx[j - 1][i], mx[j - 1][i + half])
                mn[j][i] = min(mn[j - 1][i], mn[j - 1][i + half])

        def get_value(l, r):
            length = r - l + 1
            p = lg[length]

            maximum = max(mx[p][l], mx[p][r - (1 << p) + 1])
            minimum = min(mn[p][l], mn[p][r - (1 << p) + 1])

            return maximum - minimum

        pq = []

        for l in range(n):
            heapq.heappush(pq, (-get_value(l, n - 1), l, n - 1))

        ans = 0

        while k:
            val, l, r = heapq.heappop(pq)
            ans += -val
            k -= 1

            if r > l:
                heapq.heappush(pq, (-get_value(l, r - 1), l, r - 1))

        return ans