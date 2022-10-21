class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        n = len(s)
        
        def backtracking(sub, i):
            if len(sub) == n:
                res.append(sub)
                return
            
            if s[i].isalpha():
                backtracking(sub + s[i].swapcase(), i + 1)
            
            backtracking(sub + s[i], i + 1)
        
        backtracking("", 0)
        return res