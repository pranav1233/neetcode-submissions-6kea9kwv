class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        edges = defaultdict(list)

        for source, destination, travel_time in times:
            edges[source].append((destination,travel_time))

        t = 0
        visited = set()
        minHeap = [(0,k)]

        while minHeap:
            time, node = heapq.heappop(minHeap)

            if node in visited:
                continue

            visited.add(node)

            t = time

            for nei, nei_time in edges[node]:
                if nei not in visited:
                    heapq.heappush(minHeap,(nei_time+time,nei))

        return t if len(visited) == n else -1

