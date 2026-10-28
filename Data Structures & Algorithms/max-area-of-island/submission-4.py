class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxa = 0
        row = len(grid)
        col = len(grid[0])

        def dfs(r,c):
            nonlocal total

            if r<0 or c<0 or r >= row or c >= col or grid[r][c] == 0 :
                return

            total += 1
            grid[r][c] =0 

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    total = 0
                    dfs(r,c)
                    maxa = max(maxa,total)

        return maxa