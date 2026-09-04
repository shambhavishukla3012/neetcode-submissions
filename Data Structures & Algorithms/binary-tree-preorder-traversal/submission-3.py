# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur, st = root, []
        res = []

        while cur or st:
            if cur:
                res.append(cur.val)
                st.append(cur.right)
                cur = cur.left
            else:
                cur = st.pop()

        return res