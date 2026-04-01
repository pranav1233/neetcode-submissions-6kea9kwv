class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set() 
        row,col = len(grid),len(grid[0])
        q=deque()


        def addcell(r,c): 
            if r<0 or r == row or c<0 or c == col or grid[r][c] == -1 or (r,c) in visited: 
                return 
            
            visited.add((r,c))
            q.append([r,c])



        for r in range(row): 
            for c in range(col): 
                if grid[r][c] == 0: 
                    q.append([r,c])
                    visited.add((r,c))

        dist = 0 
        while q: 
            for i in range(len(q)): 
                r,c = q.popleft()
                grid[r][c] = dist 

                addcell(r+1,c)
                addcell(r-1,c)
                addcell(r,c+1)
                addcell(r,c-1)
            dist +=1 
