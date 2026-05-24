class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        leng=len(nums)
        
        for i in range(leng):
            if nums[i] in nums[i+1:]:
                return nums[i]