class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, temp = [], []

        def backtrack(ind, total):
            if total == target:
                res.append(temp[:])
                return 

            if ind >= len(nums) or total > target:
                return 

            temp.append(nums[ind])
            backtrack(ind,total+nums[ind])
            temp.pop()
            backtrack(ind + 1, total)

        backtrack(0,0)

        return res