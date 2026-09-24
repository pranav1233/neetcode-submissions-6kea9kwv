class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []

        def backtrack(ind):
            if sum(sol) == target:
                res.append(sol[:])
                return
            elif sum(sol) > target:
                return 
            elif ind == len(nums):
                return

            sol.append(nums[ind])
            backtrack(ind)
            sol.pop()
            
            backtrack(ind + 1)

        backtrack(0)
        return res