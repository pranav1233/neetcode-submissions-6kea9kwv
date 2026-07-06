class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        for i in range(len(matrix)):
            if not matrix[i][0] <= target <= matrix[i][-1]:
                continue
            
            low = 0
            high = len(matrix[0]) - 1

            while low <= high:
                if target > matrix[i][(low+((high-low)//2))]:
                    low = (low+((high-low)//2)) + 1
                elif target < matrix[i][(low+((high-low)//2))]:
                    high = (low+((high-low)//2)) - 1
                else:
                    return True

        return False
