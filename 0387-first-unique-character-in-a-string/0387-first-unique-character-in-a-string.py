class Solution:
    def firstUniqChar(self, s: str) -> int:
        idx = -1
        dic = Counter(s)
        
        for i, char in enumerate(s):
            if dic[char] == 1:
                idx = i
                break
        
        return idx