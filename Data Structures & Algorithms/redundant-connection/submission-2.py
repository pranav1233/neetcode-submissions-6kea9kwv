class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges)+1)

        def find(node):
            
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]

            return  node

        def union(n1,n2):
            pa, pb = find(n1), find(n2)

            if pa == pb:
                return False

            if rank[pa] > rank[pb]:
                parent[pb] = pa
                rank[pa] += rank[pb]

            else:
                parent[pa] = pb
                rank[pb] += rank[pa]

            return True
 
        for a, b in edges:
            
            if not union(a,b):
                return [a,b]