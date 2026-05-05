# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def sdfs(p,q):
                    
                    if not p and not q:
                        return True
                    if not p or not q:
                        return False
                    if p.val != q.val:
                        return False 
                    return sdfs(p.left,q.left) and sdfs(p.right,q.right)
        def dfs(a,b):
            
            if not a:
                return False
            if a.val == b.val and sdfs(a,b):
                return True
                # do your operation here 
   
            return dfs(a.left,b) or dfs(a.right,b) 

        return dfs(root,subRoot)