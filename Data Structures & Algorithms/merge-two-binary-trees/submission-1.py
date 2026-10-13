# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2 
        if not root2 :
            return root1
        root1.val+=root2.val
        stack= [(root1,root2)]
        while stack:
            r1 , r2 =stack.pop()
            if r1.left and r2.left :
                    r1.left.val += r2.left.val
                    
                    stack.append((r1.left,r2.left))
            elif not r1.left :
                r1.left=r2.left
                
            if r1.right and r2.right :
                    r1.right.val += r2.right.val
                    
                    stack.append((r1.right,r2.right))
            elif not r1.right :
                r1.right=r2.right
        return root1


        
            