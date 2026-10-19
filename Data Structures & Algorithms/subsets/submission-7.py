class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res ,temp = [], []

        def backtrack(ind):
            if ind == len(nums):
                res.append(temp[:])
                return

            temp.append(nums[ind])
            backtrack(ind+1)
            temp.pop()
            backtrack(ind+1)

        backtrack(0)
        return res