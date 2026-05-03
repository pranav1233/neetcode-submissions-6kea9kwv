# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isb = True

        def dfs(node): 
            nonlocal isb
            if node is None: 
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            if left - right > 1 or right> left+1:
                isb = False
            
            return 1+max(left,right)


        dfs(root) 
        
        if isb == False:
            return False
        else:
             return True