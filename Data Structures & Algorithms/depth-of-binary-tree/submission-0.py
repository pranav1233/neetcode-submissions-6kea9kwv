# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        maxlen = 0
        curlen = 0

        def dfs(node):
            nonlocal maxlen
            nonlocal curlen
            if node is None:
                return

            curlen += 1
            maxlen=max(curlen,maxlen)

            dfs(node.left)
            dfs(node.right)

            curlen-=1
            
            
            

        dfs(root)

        return maxlen