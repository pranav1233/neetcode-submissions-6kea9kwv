class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
            
        dp1 = nums[:-1]
        dp2 = nums[1:]

        r1, r2 = 0, 0
        s1, s2 = 0, 0

        for num in dp1:
            temp = max(r1+num,r2)
            r1 = r2
            r2 = temp

        for num in dp2:
            temp = max(s1+num,s2)
            s1 = s2
            s2 = temp

        return max(r2, s2)