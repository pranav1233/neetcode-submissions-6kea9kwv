class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set() 
        q = deque() 
        time,fresh = 0,0 
        row,col = len(grid), len(grid[0])

        def makerot(r,c): 
            nonlocal fresh
            if r<0 or r == row or c<0 or c == col or (r,c) in visited or grid[r][c] != 1: 
                return 

            visited.add((r,c))
            q.append([r,c])
            grid[r][c] = 2
            fresh -=1

        for r in range(row): 
            for c in range(col): 
                if grid[r][c] == 2: 
                    q.append([r,c])
                    visited.add((r,c))
                elif grid[r][c] == 1 : 
                    fresh +=1 


        while q and fresh>0: 
            for i in range(len(q)): 
                rd,cd = q.popleft()
                visited.add((rd,cd))
                makerot(rd+1,cd)
                makerot(rd-1,cd)
                makerot(rd,cd+1)
                makerot(rd,cd-1)
            time+=1


        '''for r in range(row): 
            for c in range(col): 
                if grid[r][c] == 1: 
                    return - 1 '''
        
        return time if fresh == 0 else -1

        