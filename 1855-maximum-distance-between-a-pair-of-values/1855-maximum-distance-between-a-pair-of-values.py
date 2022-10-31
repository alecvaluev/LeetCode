class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        #brutal force
        #maxD = 0
        # 
        #for i, num in enumerate(nums1):
        #    for j, num2 in enumerate(nums2):
        #        if num2 >= num:
        #            maxD = max(maxD, j - i)
        #        
        #return maxD
        
        # 2 pointers O(n + m)
        i = j = 0
        maxD = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                maxD = max(maxD, j - i)
                j += 1
            else:
                i += 1
        
        return maxD