class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        
        for row_num in range(1, numRows):
            tmp = [0] + triangle[-1] + [0]
            row = []
            for i in range(row_num + 1):
                row.append(tmp[i] + tmp[i + 1])
        
            triangle.append(row)
        
        return triangle