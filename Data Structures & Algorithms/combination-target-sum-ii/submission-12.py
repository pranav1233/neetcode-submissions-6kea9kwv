class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
       
        inp = sorted(candidates)

        res, temp = [], []

        def backtrack(ind,total):

            if target == total:
                res.append(temp[:])
                return

            if total > target or ind >= len(inp):
                return

            if total + inp[ind] > target:
                return 

            temp.append(inp[ind])
            backtrack(ind + 1,total + inp[ind])
            temp.pop()

            while ind + 1 < len(inp) and inp[ind] == inp[ind+1]:
                ind += 1

            backtrack(ind + 1, total)

        backtrack(0,0)

        return res

