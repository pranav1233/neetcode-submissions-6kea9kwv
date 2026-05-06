# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sametree(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False 
            if p.val != q.val:
                return False 
            return sametree(p.left,q.left) and sametree(p.right,q.right)

        def dfs(a):
            if not a:
                return False

            if a.val == subRoot.val and sametree(a,subRoot):
                return True

            return dfs(a.left) or dfs(a.right) 
        
        
        return dfs(root)