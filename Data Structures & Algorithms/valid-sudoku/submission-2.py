class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            valid = set()
            for nums in board[i]:
                if nums in valid and nums != ".":
                    return False
                valid.add(nums)
        print(f"length{valid}")

        for i in range(len(board[0])):
            valid = set()
            for j in range(len(board)):
                print(f"row:{j}, column:{i}")
                if board[j][i] in valid and board[j][i] != ".":
                    return False
                valid.add(board[j][i])
        print(f"column{valid}")

        
        for row in range(0,len(board),3):
            for column in range(0,len(board[0]),3):

                valid = set()
                for row_box in range(row,row+3):
                    for column_box in range(column,column+3):
                        if board[row_box][column_box] in valid and board[row_box][column_box] != ".":
                            return False
                        valid.add(board[row_box][column_box])

        return True

        