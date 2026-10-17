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
            return None
        dic={}

        q = deque([node])
        dic[node]  = Node(node.val)
        while q  :
            node1= q.popleft()
            for n in node1.neighbors :
                if n not in dic :
                    dic[n] = Node(n.val)
                    q.append(n)

                dic[node1].neighbors.append(dic[n])
                
        return dic[node]
            

        


        
        