class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row, col = len(board), len(board[0])
        visited = set()

        def dfs(r,c):
            if r < 0 or r >= row or c < 0 or c >= col or (r,c) in visited or board[r][c] == "X":
                return 

            visited.add((r,c))

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)


        for r in range(row):
            if board[r][0] == "O" and (r,0) not in visited:
                dfs(r,0)

            if board[r][col-1] == "O" and (r,col-1) not in visited:
                dfs(r,col-1)

        for c in range(col):
            if board[0][c] =="O" and (0,c) not in visited:
                dfs(0,c)
                
            if board[row-1][c] =="O" and (row-1,c) not in visited:
                dfs(row-1,c)

        for r in range(row):
            for c in range(col):
                if (r,c) not in visited:
                    board[r][c] = "X"

            