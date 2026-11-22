from collections import deque

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def min_swaps(arr):
            n = len(arr)
            pos = {v: i for i, v in enumerate(sorted(arr))}
            visited = [False] * n
            swaps = 0
            for i in range(n):
                if visited[i] or pos[arr[i]] == i:
                    continue
                length = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = pos[arr[j]]
                    length += 1
                swaps += length - 1
            return swaps

        total = 0
        q = deque([root])
        while q:
            vals = []
            for _ in range(len(q)):
                node = q.popleft()
                vals.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            total += min_swaps(vals)
        return total