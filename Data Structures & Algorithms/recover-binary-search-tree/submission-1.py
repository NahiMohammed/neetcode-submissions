# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []

        def dfs(root):
            nonlocal res
            if not root:
                return

            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

        dfs(root)

        res.sort()
        i = 0

        def fill(root):
            nonlocal res
            nonlocal i
            if not root:
                return

            fill(root.left)
            if root.val != res[i]:
                root.val = res[i]
            i += 1
            fill(root.right)

        fill(root)
