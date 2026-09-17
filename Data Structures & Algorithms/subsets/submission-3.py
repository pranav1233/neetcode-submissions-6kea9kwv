class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res,sol = [],[]
        def backtrack(ind):
            if len(nums) == ind:
                res.append(sol[:])
                return 
            
            sol.append(nums[ind])
            backtrack(ind+1)
            sol.pop()
            backtrack(ind+1)

        backtrack(0)
        return res