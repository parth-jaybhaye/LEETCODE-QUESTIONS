from itertools import groupby

class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        s = "1" + s + "1"

        zeroGroups = []
        for c, g in groupby(s):
            if c == '0':
                zeroGroups.append(len(list(g)))

        best = 0
        for i in range(len(zeroGroups) - 1):
            best = max(best, zeroGroups[i] + zeroGroups[i + 1])

        return s.count('1') - 2 + best