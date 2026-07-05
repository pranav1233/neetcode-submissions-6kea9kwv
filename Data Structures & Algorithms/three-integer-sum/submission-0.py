class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for ind,val in enumerate(nums):
            if ind > 0 and nums[ind-1] == val:
                continue

            l , r = ind + 1, len(nums) - 1

            while l < r :
                cur= val + nums[l] + nums[r]

                if cur < 0:
                    l+=1
                elif cur > 0:
                    r-=1
                else:
                    res.append([val,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l-1] == nums[l]:
                        l+=1 
            
        return res