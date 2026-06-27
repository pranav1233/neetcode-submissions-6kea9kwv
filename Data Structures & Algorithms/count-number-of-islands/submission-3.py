class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        row , column = len(grid), len(grid[0])
        res = 0

        def dfs(r,c):
            if r < row and r >= 0 and c < column and c >= 0 and grid[r][c] == "1":
                grid[r][c] = "0"

                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)


        for r in range(row):
            for c in range(column):
                if grid[r][c]=="1":
                    #grid[r][c] = "0"
                    res += 1 
                    dfs(r,c)

        return res