class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        self.local_maxima = 0
        global_maxima = 0

        rows , cols = len(grid), len(grid[0])

        def dfs(r,c):
            if (r<0 or r>= rows or c<0 or c>= cols):
                return
            
            if grid[r][c] == 0:
                return
            
            self.local_maxima +=1
            grid[r][c] = 0
            # local_maxima = 1
            #TO do 
            dfs(r+1,c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    self.local_maxima = 0
                    dfs(r,c)
                    global_maxima = max(self.local_maxima, global_maxima)

        return global_maxima
