"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n=len(grid)
        total = sum(sum(row) for row in grid)

        if total==n*n or total==0:
            return Node(bool(total), True)
        else :
            print("s")
            mid=n//2
            topLeft=[grid[i][0:mid] for i in range(mid) ]
            bottomLeft= [grid[i][0:mid] for i in range(mid,n) ]
            topRight = [grid[i][mid:n] for i in range(mid) ]
            bottomRight= [grid[i][mid:n] for i in range(mid,n) ]
            return Node(
                False,
                False,
                self.construct(topLeft),
                self.construct(topRight),
                self.construct(bottomLeft),
                self.construct(bottomRight)
            )
        
