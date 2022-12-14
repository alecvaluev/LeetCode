class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        
        while n > 0:
        #    count += n % 2
        #    n = n >> 1
        # Alternative( a bit faster - skips all zeros)
             n = n & (n - 1)
             count += 1
        return count