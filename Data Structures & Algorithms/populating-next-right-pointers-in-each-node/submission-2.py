"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root :
            return root
        level = deque([root])
        while level :
            for _ in range(len(level)-1) :
                n = level.popleft()
                n.next = level[0]
                if n.right :
                    level.append(n.left)
                    level.append(n.right)
            n = level.popleft()
            if n.right :
                    level.append(n.left)
                    level.append(n.right)
        return root

            

        