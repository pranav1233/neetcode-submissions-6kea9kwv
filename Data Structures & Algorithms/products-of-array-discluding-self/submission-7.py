class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dummy = [1] * len(nums)
        for i in range(1,len(nums)):
            dummy[i] = dummy[i-1] * nums[i-1]
        
        temp = 1
        for i in range(len(nums) - 1, -1, -1):
            dummy[i] *= temp
            temp *= nums[i]
        
        return dummy