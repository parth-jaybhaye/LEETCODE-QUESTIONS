class Solution:
    def zigZagArrays(self, n, l, r):
        MOD = 10**9 + 7
        m = r - l + 1

        up = [0] * (m + 1)
        down = [0] * (m + 1)

        for v in range(1, m + 1):
            up[v] = v - 1
            down[v] = m - v

        for _ in range(3, n + 1):
            pref_up = [0] * (m + 1)
            pref_down = [0] * (m + 1)

            for v in range(1, m + 1):
                pref_up[v] = (pref_up[v - 1] + up[v]) % MOD
                pref_down[v] = (pref_down[v - 1] + down[v]) % MOD

            total_up = pref_up[m]

            new_up = [0] * (m + 1)
            new_down = [0] * (m + 1)

            for v in range(1, m + 1):
                new_up[v] = pref_down[v - 1]
                new_down[v] = (total_up - pref_up[v]) % MOD

            up, down = new_up, new_down

        ans = 0

        for v in range(1, m + 1):
            ans = (ans + up[v] + down[v]) % MOD

        return ans