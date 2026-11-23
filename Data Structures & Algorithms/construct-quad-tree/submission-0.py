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
        total = sum(sum(row) for row in grid) 
        n = len(grid)
        if total%(n**2) == 0  :
            return Node(bool(grid[0][0]),True)


        half = n // 2

        top_left = self.construct([row[:half] for row in grid[:half]])
        top_right = self.construct([row[half:] for row in grid[:half]])

        bottom_left = self.construct([row[:half] for row in grid[half:]])
        bottom_right = self.construct([row[half:] for row in grid[half:]])
        return Node(False , False , top_left ,top_right , bottom_left ,bottom_right)

