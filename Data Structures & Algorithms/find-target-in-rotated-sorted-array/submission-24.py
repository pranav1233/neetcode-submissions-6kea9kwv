class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0,len(nums) - 1 

        while low <= high: 
            mid = low + ((high - low)//2)
            if nums[mid] == target: 
                return mid 
            
            if nums[mid]> target and nums[high] >= target:
                if nums[mid]> nums[high]: 
                    low = mid + 1
                else: 
                    high = mid -1 

            else: 
                if target > nums[mid] and target <= nums[high]: 
                    low = mid +1 
                elif target > nums[mid] and target > nums[low]: 
                    low = mid +1
                else: 
                    high = mid - 1 
        return -1  
