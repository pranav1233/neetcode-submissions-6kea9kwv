class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph={i:[] for i in range(n)}

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited=set()
        
        def dfs(par,prev):
            if par in visited:
                return False
            
            visited.add(par)
            
            for chl in graph[par]:
                if chl != prev: 
                    if not dfs(chl,par): return False
            
            return True

        
        if not dfs(0,-1): return False 

        return True if len(visited) == n else False