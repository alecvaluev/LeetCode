class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        # O(n^2)
        #for i in range(n + 1):
        #    total = 0
        #    for num in nums:
        #        if num >= i:
        #            total += 1
        #    if total == i:
        #        return i
        
        # log(n)
        nums.sort()
        
        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l) //2
            
            x = n - mid
            if nums[mid] >= x:
                if mid == 0 or nums[mid - 1] < x:
                    return x
                else:
                    r = mid - 1
            else:
                l = mid + 1
                
        return -1