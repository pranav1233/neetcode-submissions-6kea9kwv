class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [] 
        subset = [] 
        total = 0 
        candidates.sort()

        def dfs(i,subset,total):
            if total == target and subset not in res:
                res.append(subset.copy())
                return 

            if i >= len(candidates) or total > target:
                return 

            subset.append(candidates[i])
            dfs(i+1,subset,total+candidates[i])
            subset.pop()

            while i < len(candidates) - 1 and candidates[i] == candidates [i+1]:
                i+=1

            dfs(i+1,subset,total)

        dfs(0,subset,total)
        return res             
            