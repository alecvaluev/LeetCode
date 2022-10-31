class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #triangle = [[1]]
        # 
        #for row_num in range(1, numRows):
        #    tmp = [0] + triangle[-1] + [0]
        #    row = []
        #    for i in range(row_num + 1):
        #        row.append(tmp[i] + tmp[i + 1])
        # 
        #    triangle.append(row)
        
        triangle = []
        
        for row_num in range(numRows):
            row = [1 for _ in range(row_num + 1)]
            for j in range(1, row_num):
                row[j] = triangle[-1][j - 1] + triangle[-1][j]
            triangle.append(row)
                
        return triangle