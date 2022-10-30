class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #brutal force 2 for-loops - O(n2)
        #sorting first and checking adjacent values - O(nlog(n)) - T, O(1)S
        #hashmap T-O(n), S(n)
        
        map = set()
        
        for num in nums:
            if num in map:
                return True
            map.add(num)
        return False