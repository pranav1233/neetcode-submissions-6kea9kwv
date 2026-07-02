class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}

        for ind,val in enumerate(nums):
            if (target - val) in mapp:
                return [mapp[(target - val)],ind]
            else :
                mapp[val] = ind