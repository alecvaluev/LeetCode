class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        
        # 4, 5, 8     1, 8, 9, 10
        #O(n*log(m))
        count = 0
        for num in arr1:
            
            l, r = 0, len(arr2) - 1
            while l <= r:
                mid = l + (r - l) // 2 
                
                if abs(num - arr2[mid]) <= d:
                    count += 1
                    break
                else:
                    if arr2[mid] > num:
                        r = mid - 1
                    else:
                        l = mid + 1
        return len(arr1) - count
            