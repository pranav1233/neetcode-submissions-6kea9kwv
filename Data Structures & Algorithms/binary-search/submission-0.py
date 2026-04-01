class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1 

        while low<= high: 
            if target < nums[low+((high - low)//2)]: 
                high = (low+((high-low)//2)) -1 
            elif target > nums[low+((high - low)//2)]: 
                low = (low+((high - low)//2)) +1
            else: 
                return (low+((high - low)//2))
        
        return  -1