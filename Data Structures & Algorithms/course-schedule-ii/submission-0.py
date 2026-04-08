class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visit=set()
        res=[]
        graph ={i:[] for i in range(numCourses)}

        for u,v in prerequisites: 
            graph[u].append(v)

        

        def dfs(crs): 
            if crs in visit: 
                return False 
            if graph[crs] == [] and crs not in res:
                res.append(crs)
                return True
            if graph[crs] == [] and crs in res:
                return True
            

            visit.add(crs)
            for pre in graph[crs]: 
                if not dfs(pre): return False
            
            graph[crs] = []
            res.append(crs)
            visit.remove(crs)
            
            return True



        

        for crs in range(numCourses): 
            if not dfs(crs): return []

        return res