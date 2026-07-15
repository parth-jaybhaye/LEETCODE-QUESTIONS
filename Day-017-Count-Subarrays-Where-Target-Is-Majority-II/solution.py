class Solution:
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)
        OFFSET = n + 1
        bit_size = 2 * n + 2
        tree = [0] * (bit_size + 1)

        def update(idx, delta):
            while idx <= bit_size:
                tree[idx] += delta
                idx += idx & -idx

        def query(idx):
            total = 0
            while idx > 0:
                total += tree[idx]
                idx -= idx & -idx
            return total

        update(OFFSET, 1)

        prefix = 0
        ans = 0

        for num in nums:
            if num == target:
                prefix += 1
            else:
                prefix -= 1

            ans += query(prefix + OFFSET - 1)
            update(prefix + OFFSET, 1)

        return ans