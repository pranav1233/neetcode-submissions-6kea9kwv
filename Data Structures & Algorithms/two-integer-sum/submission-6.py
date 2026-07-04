class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for ind,val in enumerate(nums):
            if target-val in res:
                return [res[target-val],ind]
            res[val] = ind
