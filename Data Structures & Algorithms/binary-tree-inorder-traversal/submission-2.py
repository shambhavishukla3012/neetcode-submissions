# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # res = []

        # def inorder(root):
        #     if not root:
        #         return

        #     inorder(root.left)
        #     res.append(root.val)
        #     inorder(root.right)
        #     return res

        # inorder(root)
        # return res


        res = []
        st = []
        while root or st:
            while root:
                st.append(root)
                root = root.left
            root = st.pop()
            res.append(root.val)
            root = root.right
        return res
