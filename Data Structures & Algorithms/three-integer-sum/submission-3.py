class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        if len(nums) == 3 and sum(nums) ==0:
            return [nums]
        
        i = 0

        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            l = i + 1
            r = len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and  nums[l] == nums[l-1]:
                        l += 1

                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1

                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
            
 
        return res