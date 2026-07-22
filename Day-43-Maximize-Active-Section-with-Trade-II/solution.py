class SparseTable:
    def __init__(self, nums):
        self.n = len(nums)
        if self.n == 0:
            self.st = []
            return

        self.st = [[0] * (self.n + 1) for _ in range(self.n.bit_length() + 1)]
        self.st[0] = list(nums)

        for i in range(1, self.n.bit_length() + 1):
            for j in range(self.n - (1 << i) + 1):
                self.st[i][j] = max(
                    self.st[i - 1][j],
                    self.st[i - 1][j + (1 << (i - 1))]
                )

    def query(self, l, r):
        if l > r or not self.st:
            return 0

        i = (r - l + 1).bit_length() - 1
        return max(self.st[i][l], self.st[i][r - (1 << i) + 1])


class Solution:
    def maxActiveSectionsAfterTrade(self, s, queries):
        ones = s.count('1')
        zeroGroups, zeroGroupIndex = self._getZeroGroups(s)

        if not zeroGroups:
            return [ones] * len(queries)

        st_merge = SparseTable(self._getZeroMergeLengths(zeroGroups))
        st_single = SparseTable([g[1] for g in zeroGroups])

        def getMaxActiveSections(l, r):
            g_l = zeroGroupIndex[l]
            g_r = zeroGroupIndex[r]

            left = 0
            if s[l] == '0' and g_l != -1:
                left = zeroGroups[g_l][1] - (l - zeroGroups[g_l][0])

            right = 0
            if s[r] == '0' and g_r != -1:
                right = r - zeroGroups[g_r][0] + 1

            first_full_g = g_l + 1 if s[l] == '0' else g_l
            last_full_g = g_r - 1 if s[r] == '0' else g_r

            max_gain = 0

            if s[l] == '0' and g_l == g_r:
                max_gain = max(max_gain, r - l + 1)
            else:
                max_gain = max(max_gain, left, right)

                if first_full_g <= last_full_g:
                    max_gain = max(max_gain, st_single.query(first_full_g, last_full_g))

            if s[l] == '0' and s[r] == '0' and g_l + 1 == g_r:
                max_gain = max(max_gain, left + right)

            if s[l] == '0' and g_l + 1 < len(zeroGroups) and g_l + 1 <= last_full_g:
                max_gain = max(max_gain, left + zeroGroups[g_l + 1][1])

            if s[r] == '0' and g_r - 1 >= 0 and g_r - 1 >= first_full_g:
                max_gain = max(max_gain, right + zeroGroups[g_r - 1][1])

            startAdjacent = first_full_g
            endAdjacent = last_full_g - 1

            if startAdjacent <= endAdjacent:
                max_gain = max(max_gain, st_merge.query(startAdjacent, endAdjacent))

            return ones + max_gain

        return [getMaxActiveSections(l, r) for l, r in queries]

    def _getZeroGroups(self, s):
        zeroGroups = []
        zeroGroupIndex = []

        for i in range(len(s)):
            if s[i] == '0':
                if i > 0 and s[i - 1] == '0':
                    zeroGroups[-1][1] += 1
                else:
                    zeroGroups.append([i, 1])

            zeroGroupIndex.append(len(zeroGroups) - 1)

        return zeroGroups, zeroGroupIndex

    def _getZeroMergeLengths(self, zeroGroups):
        return [
            zeroGroups[i][1] + zeroGroups[i + 1][1]
            for i in range(len(zeroGroups) - 1)
        ]