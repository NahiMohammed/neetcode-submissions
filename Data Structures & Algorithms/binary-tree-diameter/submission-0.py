# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(root) :
            if not root:
                return 0

            return 1 + max(depth(root.left), depth(root.right))
        if not root : 
            return 0
        left = 0 
        if root.left :
            left = depth(root.left)
        right = 0 
        if root.right :
            right = depth(root.right)
        curr =  left +right
        sub = max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
        return max(curr,sub)

        
        