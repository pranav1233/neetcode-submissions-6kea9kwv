class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
       
        res,temp = [], [] 

        nums = sorted(candidates)

        def backtrack(ind,total):
            if total == target:
                res.append(temp[:])
                return 
            if total > target or ind >= len(nums):
                return 

            temp.append(nums[ind])
            backtrack(ind+1,total + nums[ind])
            temp.pop()

            while ind + 1 < len(nums) and nums[ind] == nums[ind + 1]:
                ind += 1

            backtrack(ind + 1, total)

        backtrack(0,0)

        return res
     