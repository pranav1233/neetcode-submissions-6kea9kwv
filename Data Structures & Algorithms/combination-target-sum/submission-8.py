class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res , temp = [], []

        def backtrack(ind):
            if sum(temp) == target:
                res.append(temp[:])
                return 
            if sum(temp) > target or ind == len(nums):
                return 

            temp.append(nums[ind])
            backtrack(ind)
            temp.pop()
            backtrack(ind+1)

        backtrack(0)
        return res