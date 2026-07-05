class Solution:
    def maxArea(self, heights: List[int]) -> int:
        h=heights
        l, r = 0, len(heights) - 1
        max_area = 0 

        while l<r:

            area = (r-l) * min(h[l],h[r])
            print(area)
            max_area = max(max_area, area)
            print("max area ",max_area)

            if h[l] <= h[r]:
                l+=1
            elif h[l] >= h[r]:
                r-=1
            
        return max_area

