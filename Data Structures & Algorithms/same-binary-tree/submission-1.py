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
            if a is None or b is None:
                return False 
            if a.val != b.val:
                return False 

            left = dfs(a.left,b.left)
            right = dfs(a.right,b.right)

            if left is True and right is True:
                return True 
            else:
                return False

        return dfs(p,q)