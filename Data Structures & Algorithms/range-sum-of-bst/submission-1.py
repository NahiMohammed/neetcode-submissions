class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        res = 0

        while stack:
            node = stack.pop()
            if not node:
                continue

            if low <= node.val <= high:
                res += node.val
            if node.val > low:
                stack.append(node.left)
            if node.val < high:
                stack.append(node.right)

        return res