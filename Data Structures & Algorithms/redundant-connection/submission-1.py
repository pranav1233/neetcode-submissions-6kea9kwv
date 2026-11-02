class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = [i for i in range(len(edges) + 1)]

        def find(node):
            
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]

            return  node

        for a, b in edges:
            pa, pb = find(a),find(b)

            if pa == pb:
                return [a,b]

            parent[pb] = pa