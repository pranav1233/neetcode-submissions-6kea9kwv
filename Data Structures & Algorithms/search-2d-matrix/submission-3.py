class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        column = len(matrix[0])

        if row > 1 : 
            low = 0
            high = row - 1

            while low <= high: 
                middle = low + ((high - low)//2)
                if target < matrix[middle][0]: 
                    high = middle - 1
                elif target > matrix[middle][-1]: 
                    low = middle + 1 
                else: 
                    break 
        else: 
            middle = 0 

        actual_matrix = matrix[middle]

        l = 0 
        h = column - 1 

        while l <= h : 
            mid = l+((h-l)//2)
            if target < actual_matrix[mid]:
                h = mid -1 
            elif target > actual_matrix[mid] : 
                l = mid +1 
            else: 
                return True 
        return False 