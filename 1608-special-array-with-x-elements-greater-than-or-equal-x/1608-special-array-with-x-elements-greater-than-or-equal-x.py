class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n + 1):
            total = 0
            for num in nums:
                if num >= i:
                    total += 1
            if total == i:
                return i
        
        return -1