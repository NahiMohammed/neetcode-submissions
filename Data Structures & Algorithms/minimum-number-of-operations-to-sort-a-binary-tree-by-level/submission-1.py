# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def min_swaps(arr) :
            pos = {v : i for i , v in enumerate(sorted(arr))}
            visited = [False]*len(arr)
            swaps = 0
            for i in range(len(arr)) :
                if visited[i] or pos[arr[i]] == i :
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

        