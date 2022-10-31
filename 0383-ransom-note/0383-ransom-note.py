class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # space - O(n*m), time O(n + m)
        #noteDict = Counter(ransomNote)
        #magDict = Counter(magazine)
        # 
        #for letter, count in noteDict.items():
        #    if not(letter in magDict and count <= magDict[letter]):
        #        return False
        #return True
        
        # space O(m)
        dic = {}
        for char in magazine:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1
        
        for char in ransomNote:
            if char not in dic or dic[char] == 0:
                return False
            else:
                dic[char] -= 1
        
        return True