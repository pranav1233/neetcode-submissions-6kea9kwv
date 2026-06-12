class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lst=[]
        res=[]
        for point in points:
            dist=((point[0])**2 + (point[1]**2))**0.5
            newlst=[dist]
            newlst.append(point)
            lst.append(newlst)

        heapq.heapify(lst)

        for i in range(k):
            closest_point=heapq.heappop(lst)
            res.append(closest_point[1])

        return res
