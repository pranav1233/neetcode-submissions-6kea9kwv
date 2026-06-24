class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for ind,val in enumerate(nums):
            
            if target-val in dict:
                return [dict[target-val],ind]

            dict[val] = ind

