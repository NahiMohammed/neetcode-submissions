class Solution:
    def reverseOddLevels(self, root):
        def dfs(a, b, level):
            if not a:
                return
            if level % 2 == 1:
                a.val, b.val = b.val, a.val
            dfs(a.left, b.right, level + 1)
            dfs(a.right, b.left, level + 1)
        dfs(root.left, root.right, 1)
        return root