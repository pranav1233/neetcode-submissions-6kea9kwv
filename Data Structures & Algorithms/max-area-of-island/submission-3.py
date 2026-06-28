class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row,column = len(grid),len(grid[0])
        maxim = 0

        def dfs(r,c,):
            nonlocal area
            if r >= 0 and r < row and c >= 0 and c < column and grid[r][c] == 1:
                area += 1
                grid[r][c] = 0
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)

            
 
        for r in range(row):
            for c in range(column):
                if grid[r][c] == 1:
                    area = 0
                    dfs(r,c)
                    maxim = max(maxim,area)


        return maxim

