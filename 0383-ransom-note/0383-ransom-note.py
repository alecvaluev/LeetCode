class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        noteDict = Counter(ransomNote)
        magDict = Counter(magazine)
        
        for letter, count in noteDict.items():
            if not(letter in magDict and count <= magDict[letter]):
                return False
        return True