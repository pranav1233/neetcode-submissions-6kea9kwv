# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        q=deque()
        res=[]

        q.append(root)

        while q:
            lis = []
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if node:
                    lis.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if lis:
                res.append(lis)
        return res