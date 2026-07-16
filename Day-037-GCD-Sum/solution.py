class Solution:
    def gcdSum(self, nums):
        def custom_gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(nums)
        prefixGcd = []
        current_max = nums[0]
        
        for num in nums:
            current_max = max(current_max, num)
            prefixGcd.append(custom_gcd(num, current_max))
            
        prefixGcd.sort()
        
        total_sum = 0
        left = 0
        right = n - 1
        
        while left < right:
            total_sum += custom_gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
            
        return total_sum
