# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = -10001 

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left<0 and right<0:
                res=max(res,node.val)
                return node.val
            elif left <0 and right>=0:
                res=max(res,node.val+right)
                return node.val+right
            elif left >=0 and right<0:
                res=max(res,node.val+left)
                return node.val+left
            elif left>=0 and right>=0:
                res=max(res,node.val+right+left)
                return max(node.val+right,node.val+left)


        dfs(root)

        return res
