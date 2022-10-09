class Solution:
    def reverse(self, nums: List[int], left: int, right: int):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        # reverse whole array
        self.reverse(nums, 0, n - 1)
        #reverse part
        self.reverse(nums, 0, k - 1)
        #right part
        self.reverse(nums, k, n - 1)

    