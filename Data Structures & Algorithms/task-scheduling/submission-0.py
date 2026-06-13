class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        maxheap = [vals for vals in count.values()]
        heapq.heapify_max(maxheap)
        q=deque()
        time = 0

        while maxheap or q:
            time+=1
            if maxheap:
                pop = heapq.heappop_max(maxheap) - 1
                if pop:
                    q.append([pop,time+n])
            if q and q[0][1] == time:
                qpop = q.popleft()
                heapq.heappush_max(maxheap,qpop[0])
        
        return time