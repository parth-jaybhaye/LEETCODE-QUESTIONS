class Solution(object):
    def sumAndMultiply(self, s, queries):
        MOD = 10**9 + 7

        n = len(s)

        values = []
        prefix_sum = [0] * (n + 1)
        prefix_num = [0] * (n + 1)
        count = [0] * (n + 1)

        for i, ch in enumerate(s):
            digit = int(ch)

            prefix_sum[i + 1] = prefix_sum[i]
            prefix_num[i + 1] = prefix_num[i]
            count[i + 1] = count[i]

            if digit != 0:
                prefix_sum[i + 1] += digit
                prefix_num[i + 1] = (prefix_num[i] * 10 + digit) % MOD
                count[i + 1] += 1

        ans = []

        for l, r in queries:
            if count[r + 1] == count[l]:
                ans.append(0)
                continue

            num = 0
            total = 0

            for i in range(l, r + 1):
                if s[i] != '0':
                    digit = int(s[i])
                    num = (num * 10 + digit) % MOD
                    total += digit

            ans.append((num * total) % MOD)

        return ans