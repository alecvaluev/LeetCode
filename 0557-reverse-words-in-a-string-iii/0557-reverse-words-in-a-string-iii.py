class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()[::-1]
        s = " ".join(arr)
        s = s[::-1]
        return s
    