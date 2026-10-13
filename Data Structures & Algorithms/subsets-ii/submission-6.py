class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
          
        res, temp = [],[]

        n = sorted(nums)

        def backtrack(ind):
            if ind >= len(n):
                res.append(temp[:])
                return 

            temp.append(n[ind])
            backtrack(ind+1)
            temp.pop()

            while ind + 1 < len(n) and n[ind] == n[ind+1]:
                ind += 1

            backtrack(ind+1)

        backtrack(0)

        return res