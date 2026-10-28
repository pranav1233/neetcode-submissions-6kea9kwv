class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)

        if total % 2 != 0:
            return False

        total = total / 2

        temp = []

        def dfs(i,suma):
            if suma == total:
                return True

            if i == len(nums):
                return False

            res = dfs(i+1,suma+nums[i])
            res = res or dfs(i+1,suma)
            return res

        return dfs(0,0)
            