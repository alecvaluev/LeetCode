class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        solders = [0] * len(mat)
        
        for i, row in enumerate(mat):
            solders[i] = (sum(row), i)
        
        solders.sort()
        
        return (i[1] for i in solders[:k]) 
        