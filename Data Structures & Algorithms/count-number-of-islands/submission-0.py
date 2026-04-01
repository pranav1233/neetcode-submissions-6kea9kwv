class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set() 
        
        row,column = len(grid),len(grid[0])

        count = 0 

        def dfs(r,c): 

            directions = [[1,0], [-1,0],[0,1],[0,-1]]

            for dr,dc in directions: 
                rn,cn = r+dr , c+dc 

                if rn in range(row) and cn in range(column) and grid[rn][cn]=="1" and (rn,cn) not in visited:
                    visited.add((rn,cn))
                    dfs(rn,cn)
                    

        for r in range(row): 
            for c in range(column):
                if grid[r][c] == "1" and (r,c) not in visited: 
                    count +=1 
                    #visited.add((r,c))
                    dfs(r,c)
        
        return count
