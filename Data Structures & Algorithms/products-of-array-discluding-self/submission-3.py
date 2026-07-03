class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [0]*len(nums)

        for i in range(len(nums)):
            left = nums[:i]
            right = nums[i+1:]
            '''print(left)
            print(right)'''

            l_pro = 1
            if len(left) > 0 : 
                for items in left:
                    l_pro *= items
            
            r_pro = 1
            if len(right) > 0 :
                for items in right:
                    r_pro *= items

            res[i] = l_pro * r_pro

        return res