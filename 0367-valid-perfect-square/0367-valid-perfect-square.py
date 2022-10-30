class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        #brute for loop from 0 to num => O(sqrt(n)) 
        #log(n)
        l, r = 0, num
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid < num:
                l = mid + 1
            elif mid * mid > num:
                r = mid - 1
            else:
                return True
        return False
        
        