class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        res = []
        stack = [root]
        while stack:
            item = stack.pop()
            if isinstance(item, str):      # a piece of text: "(", ")" or "()"
                res.append(item)
                continue
            res.append(str(item.val))
            if item.right:                 # pushed first, so it is handled last
                stack.append(")")
                stack.append(item.right)
                stack.append("(")
            if item.left:
                stack.append(")")
                stack.append(item.left)
                stack.append("(")
            elif item.right:               # no left child, but a right child
                stack.append("()")
        return "".join(res)