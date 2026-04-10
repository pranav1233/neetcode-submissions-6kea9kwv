class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        visited = set()
        graph={i:[] for i in range(n)}

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)


        def dfs(i,prev):
            if i in visited:
                return
            
            visited.add(i)
            for chl in graph[i]:
                if chl != prev:
                    dfs(chl,i)           




        for i in graph:
            if i not in visited:
                dfs(i,-1)
                res+=1

        return res