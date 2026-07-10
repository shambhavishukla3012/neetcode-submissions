# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q =collections.deque([root])
        res = []

        while q:
            rightside = None
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    rightside = node.val
                    q.append(node.left)
                    q.append(node.right)
            if rightside:
                res.append(rightside)       

        return res