class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l,r = 0 , len(numbers) - 1

        while l < r:
            cur_sum = numbers[r] + numbers[l]
            if target > cur_sum :
                l += 1 
            elif target < cur_sum:
                r -= 1
            else:
                return[l+1,r+1]
            
        return []