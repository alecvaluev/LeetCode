class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 1
        last = arr[len(arr) - 1]
        
        while k:
            if i in arr:
                i += 1
            else:
                i += 1
                k -= 1
        
       
            
        return i - 1
                
                        