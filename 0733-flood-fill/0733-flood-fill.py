class Solution:
    def dfs(self, image, sc, sr, initColor, color):
        
            if sc < 0 or sc >= len(image[0]) or sr < 0 or sr >= len(image) or image[sr][sc] != initColor:
                return

            image[sr][sc] = color        

            self.dfs(image, sc - 1, sr, initColor, color)
            self.dfs(image, sc + 1, sr, initColor, color)
            self.dfs(image, sc, sr - 1, initColor, color)
            self.dfs(image, sc, sr + 1, initColor, color)
            
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color: return image
        self.dfs(image, sc, sr, image[sr][sc], color)
        return image
        
   