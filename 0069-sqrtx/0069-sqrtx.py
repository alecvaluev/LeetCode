class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x <= 1:
            return x
        
        l, r = 0, x
        ans = 0
        
        while l <= r:
            mid = l + (r - l) // 2
            value = mid * mid
            
            if(value == x ):
                return mid
            if(value < x):
                l = mid + 1
                ans = mid
            else:
                r = mid - 1
                
        return ans