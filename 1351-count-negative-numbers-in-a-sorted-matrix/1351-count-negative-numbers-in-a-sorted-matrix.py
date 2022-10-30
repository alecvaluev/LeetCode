class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        c = 0
        r = ROWS -1 
        total = 0
        
        while c < COLS and r >= 0:
            if grid[r][c] < 0:
                total += (COLS - c)
                r -= 1
            else:
                c += 1
        return total