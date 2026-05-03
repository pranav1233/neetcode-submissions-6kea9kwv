# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        

        def dfs(a,b): 
            if a is None and b is None:
                return True
            if not a  or not b or a.val != b.val  :
                return False

            left = (dfs(a.left, b.left))
            right = (dfs(a.right, b.right))

            return left and right

                

        return dfs(p,q)

        
        
