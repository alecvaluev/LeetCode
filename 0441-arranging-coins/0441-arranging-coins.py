class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n
        res = 0
        
        while l <= r:
            mid = l + (r - l) //2
            coints = (mid / 2)*(mid + 1)
            if coints > n:
                r = mid - 1
            else:
                l = mid + 1
                res = max(res, mid)
        return res