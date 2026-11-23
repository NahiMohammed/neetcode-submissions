class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(node):
            nonlocal res
            if not node:
                return 0

            # ignore negative paths (take 0 instead)
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # best path passing through this node (uses both sides)
            res = max(res, node.val + left + right)

            # best path going down from this node (only one side)
            return node.val + max(left, right)

        dfs(root)
        return res