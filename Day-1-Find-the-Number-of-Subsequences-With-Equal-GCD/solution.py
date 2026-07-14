from collections import defaultdict
import math

class Solution:
    def subsequencePairCount(self, nums: list[int]) -> int:
        MOD = 1_000_000_007
        state_counts = defaultdict(int)
        state_counts[(0, 0)] = 1
        
        for num in nums:
            current_states = list(state_counts.items())
            for (g1, g2), count in current_states:
                next_g1 = math.gcd(g1, num) if g1 else num
                state_counts[(next_g1, g2)] = (state_counts[(next_g1, g2)] + count) % MOD
                
                next_g2 = math.gcd(g2, num) if g2 else num
                state_counts[(g1, next_g2)] = (state_counts[(g1, next_g2)] + count) % MOD
                
        total_valid_pairs = 0
        for (g1, g2), count in state_counts.items():
            if g1 > 0 and g1 == g2:
                total_valid_pairs = (total_valid_pairs + count) % MOD
                
        return total_valid_pairs