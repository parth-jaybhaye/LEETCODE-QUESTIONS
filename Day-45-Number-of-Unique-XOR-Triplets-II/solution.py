class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        unique_nums = list(set(nums))
        n = len(unique_nums)
        
        triplet_xors = set(unique_nums)
        pair_xors = set()
        
        for i in range(n):
            for j in range(i + 1, n):
                pair_xors.add(unique_nums[i] ^ unique_nums[j])
        
        for p_xor in pair_xors:
            for num in unique_nums:
                triplet_xors.add(p_xor ^ num)
                
        return len(triplet_xors)
