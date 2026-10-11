"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        stack=[root]
        visited=[False]
        res=[]
        while stack :
            curr , v = stack.pop()  , visited.pop()
            if curr :
                if v :
                    res.append(curr.val)
                else :
                    stack.append(curr)
                    visited.append(True)
                    for c in range(len(curr.children)-1,-1,-1) :
                        stack.append(curr.children[c])
                        visited.append(False)
        return res


        