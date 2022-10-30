class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # T-O(n), S-O(1)
        l, r = 0, len(s) - 1
        
        while l < r:
            s[l], s[r] = s[r], s[l] 
            l, r = l + 1, r - 1
            
        # Alternative: T/S O(n) - use stack to read in reverse and replace each char
        
        # Recursive: TS O(n)