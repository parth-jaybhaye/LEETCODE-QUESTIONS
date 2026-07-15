from collections import Counter

class Solution:
    def maximumLength(self, nums):
        count = Counter(nums)
        max_num = max(nums)

        if 1 in count:
            ans = count[1] if count[1] % 2 == 1 else count[1] - 1
        else:
            ans = 1

        for num in nums:
            if num == 1:
                continue

            length = 0
            x = num

            while x <= max_num and count.get(x, 0) >= 2:
                length += 2
                x *= x

            if count.get(x, 0):
                ans = max(ans, length + 1)
            else:
                ans = max(ans, length - 1)

        return ans