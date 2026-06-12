class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lst=[]
        res=[]
        for x,y in points:
            dist=((x)**2 + (y)**2)**0.5
            lst.append([dist,[x,y]])

        heapq.heapify(lst)

        for i in range(k):
            closest_point=heapq.heappop(lst)
            res.append(closest_point[1])

        return res
