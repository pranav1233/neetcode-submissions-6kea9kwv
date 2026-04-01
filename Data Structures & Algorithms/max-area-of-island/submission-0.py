class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        row,column = len(grid) , len(grid[0])
        big = 0 
        marea = 0 

        def dfs(r,c): 
            nonlocal area
            if ((r,c) in visited): 
                return 
            visited.add((r,c))
            area +=1 

            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr,dc in directions: 
                nr,nc = r+dr,c+dc 

                if nr in range(row) and nc in range(column) and (grid[nr][nc] == 1) and (nr,nc) not in visited: 
                    '''visited.add((nr,nc))
                    area += 1'''
                    dfs(nr,nc)


                

        for r in range(row): 
            for c in range(column): 

                if grid[r][c] == 1 and (r,c) not in visited: 
                    '''visited.add((r,c))'''
                    area = 0
                    
                    dfs(r,c)
                    marea = max(marea,area)
        return marea


        