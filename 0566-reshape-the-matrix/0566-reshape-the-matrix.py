class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        if r*c != ROWS * COLS:
            return mat
        
        reshaped = [[0 for _ in range(c)] for _ in range(r)]
        #tmp = []
        # 
        # for i in range(ROWS):
        #     for j in range(COLS):
        #         tmp.append(mat[i][j])
        # print(tmp)
        # k = 0
        
        for i in range(ROWS*COLS):
            reshaped[i // c][i % c] = mat[i // COLS][i % COLS]
                
        return reshaped