class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = []

        def backtrack(r,c,i):
            if i == len(word):
                return True

            if r < 0 or r == len(board) or c < 0 or c == len(board[0]):
                return False

            if  (r,c) in visited:
                return False

            if board[r][c] != word[i]:
                return False

            visited.append((r,c))
            
            res = (backtrack(r+1,c,i+1) or 
            backtrack(r-1,c,i+1) or 
            backtrack(r,c+1,i+1) or 
            backtrack(r,c-1,i+1))

            visited.remove((r,c))

            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                
                f = backtrack(i,j,0)
                
                if f is True:
                    return True

        return False