# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        qu1 = deque([p])
        qu2 = deque([q])

        while qu1 and qu2:
            n1 = qu1.popleft()
            n2 = qu2.popleft()

            if n1.val != n2.val:
                return False

            # Left children
            if n1.left and n2.left:
                qu1.append(n1.left)
                qu2.append(n2.left)
            elif n1.left or n2.left:
                return False

            # Right children
            if n1.right and n2.right:
                qu1.append(n1.right)
                qu2.append(n2.right)
            elif n1.right or n2.right:
                return False

        return True



        