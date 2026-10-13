class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
          
        res , temp = [], []

        def backtrack(ind):
            if ind == len(nums):
                ntemp = sorted(temp)
                if ntemp not in res:
                    res.append(ntemp[:])

                return 

            temp.append(nums[ind])
            backtrack(ind+1)
            temp.pop()
            backtrack(ind+1)

        backtrack(0)

        return res