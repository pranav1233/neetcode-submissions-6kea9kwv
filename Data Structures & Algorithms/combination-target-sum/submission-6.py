class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []

        def backtrack(ind,summ):
            if summ == target:
                res.append(sol[:])
                return
            elif summ > target:
                return 
            elif ind == len(nums):
                return

            sol.append(nums[ind])
            summ += nums[ind]
            backtrack(ind,summ)
            rem = sol.pop()
            summ -= rem
            backtrack(ind + 1,summ)

        backtrack(0,0)
        return res