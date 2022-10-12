class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        i = 0
        
        def swap(l, i):
            nums[l], nums[i] = nums[i], nums[l]
            
        while(i <= r):
            if(nums[i] == 0):
                swap(l, i)
                l += 1
            if(nums[i] == 2):
                swap(r, i)
                r -= 1
                i -= 1
            i += 1    
            