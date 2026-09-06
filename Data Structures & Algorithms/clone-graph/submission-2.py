"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node :
            return node
        clone={}       
        queu=deque([node])
        visited=set()
        original = node
        while queu :
            node = queu.popleft()
            if node in visited :
                continue
            if node not in clone :

                clone[node] =Node(node.val)
            visited.add(node)
            for n in node.neighbors :
                if n not in clone:
                    clone[n] = Node(n.val)
                clone[node].neighbors.append(clone[n])
                if n not in visited :

                    queu.append(n)
        return clone[original]

        
            

