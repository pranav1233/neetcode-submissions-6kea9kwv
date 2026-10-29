class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        i = 0 
        l = len(numbers) - 1

        while i < l:
            if numbers[i] + numbers[l] == target:
                return [i+1, l+1]

            if numbers[i] + numbers[l] < target:
                i = i+1

            if numbers[i] + numbers[l] > target:
                l -= 1

        