class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        dp = [0] *len(nums)

        dp[0], dp[1] = nums[0], nums[1]

        for i in range(2,len(nums)):
            for j in range(2,4):
                if i-j >= 0:
                    dp[i] = max(dp[i], nums[i] + dp[i-j])

        print(dp)
        return max(dp[-1], dp[-2])