class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        # int((('{0:032b}'.format(n))[::-1]),2)
        
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i)) 
        return res