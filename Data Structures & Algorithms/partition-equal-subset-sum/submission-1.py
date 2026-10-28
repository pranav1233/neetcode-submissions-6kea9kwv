class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)

        if total % 2 != 0:
            return False

        total = total / 2

        res, temp = [],[]

        def dfs(i,suma):
            if suma == total:
                return True

            if i == len(nums):
                return False

            temp.append(nums[i])
            res = dfs(i+1,suma+nums[i])
            temp.pop()
            res = res or dfs(i+1,suma)
            return res

        return dfs(0,0)
            