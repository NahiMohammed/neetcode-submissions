from collections import deque

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        def max_level(node):
            if node is None:
                return 0
            return 1 + max(max_level(node.left), max_level(node.right))

        h = max_level(root)          # call it once, not on every loop
        level = 0
        q = deque([root])

        while level < h - 1:         # only the levels before the last one
            if len(q) != 2**level:   # these levels must be full
                return False

            if level == h - 2:
                # the children of this level are the last level
                gap = False
                for node in q:
                    for child in (node.left, node.right):
                        if child is None:
                            gap = True
                        elif gap:    # a real node after a gap
                            return False
                return True

            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1

        return True