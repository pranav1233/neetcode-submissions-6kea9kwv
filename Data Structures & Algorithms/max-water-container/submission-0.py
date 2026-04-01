class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r =0, (len(heights)-1)
        maxv = 0

        while r > l : 

            if heights[r] > heights[l]: 
                vol = ((r-l)*heights[l])
                l+=1 
            elif heights[r] < heights[l]:
                vol = ((r-l)*heights[r])
                r-=1 
            else: 
                vol = ((r-l)*heights[l])
                r-=1 
            maxv = max(maxv,vol)

        return maxv
