class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row = len(grid)
        col = len(grid[0])
        INF = 2147483647
        q = deque()

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    q.append((r,c))

        while q:
            r,c = q.popleft()

            for cr,cc in((1,0),(-1,0),(0,1),(0,-1)):
                nr,nc = r+cr,c+cc
                if nr >= 0 and nr < row and nc >=0 and nc < col and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr,nc))