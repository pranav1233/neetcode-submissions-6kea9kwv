class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visit=set()

        for i in range(numCourses):
            graph[i] =[]
        for u,v in prerequisites:
            graph[u].append(v)


        def dfs(crs): 
            #base cases
            if crs in visit:
                return False
            if graph[crs] == []:
                return True

            visit.add(crs)
            for pre in graph[crs]: 
                if not dfs(pre): return False

            graph[crs] =[]
            visit.remove(crs)
            return True


        for items in graph:
            if not dfs(items): return False 
        return True
            