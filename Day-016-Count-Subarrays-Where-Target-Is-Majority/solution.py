class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)
        self.size = size

    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total


class Solution:
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)
        offset = n + 1

        bit = FenwickTree(2 * n + 2)
        bit.update(offset, 1)

        prefix = 0
        ans = 0

        for num in nums:
            if num == target:
                prefix += 1
            else:
                prefix -= 1

            ans += bit.query(prefix + offset - 1)
            bit.update(prefix + offset, 1)

        return ans