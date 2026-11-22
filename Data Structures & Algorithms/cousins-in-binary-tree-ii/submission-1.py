from collections import deque

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        root.val = 0              # root has no cousins
        q = deque([root])

        while q:
            # 1) sum of the whole next level (using the original values)
            next_level_sum = 0
            for n in q:
                if n.left:
                    next_level_sum += n.left.val
                if n.right:
                    next_level_sum += n.right.val

            for _ in range(len(q)):
                n = q.popleft()

                siblings_sum = 0
                if n.left:
                    siblings_sum += n.left.val
                if n.right:
                    siblings_sum += n.right.val

                if n.left:
                    n.left.val = next_level_sum - siblings_sum
                    q.append(n.left)
                if n.right:
                    n.right.val = next_level_sum - siblings_sum
                    q.append(n.right)

        return root