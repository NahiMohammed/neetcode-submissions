    def rob(self, root: Optional[TreeNode]) -> int:
        cache = { None : 0 }

        def dfs(root):
            if root in cache:
                return cache[root]

            cache[root] = root.val
            if root.left:
                cache[root] += dfs(root.left.left) + dfs(root.left.right)
            if root.right:
                cache[root] += dfs(root.right.left) + dfs(root.right.right)

            cache[root] = max(cache[root], dfs(root.left) + dfs(root.right))
            return cache[root]

        return dfs(root)