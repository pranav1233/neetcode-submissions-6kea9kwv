# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q=deque()
        res=[]
        q.append(root)
        while q:
            qlen=len(q)
            lis =[]
            for i in range(qlen):
                node=q.popleft()
                if node:
                    lis.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if lis:
                res.append(lis[-1])

        return res
