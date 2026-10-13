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
        dummy = TreeNode(root1.val+root2.val)
        stack= [(root1,root2,dummy)]
        while stack:
            r1 , r2 , r =stack.pop()
            if r1.left and r2.left :
                    r.left = TreeNode(r1.left.val+r2.left.val)
                    
                    stack.append((r1.left,r2.left,r.left))
            elif not r2.left :
                r.left=r1.left
            else :
                r.left=r2.left
            if r1.right and r2.right :
                r.right = TreeNode(r1.right.val+r2.right.val)
                    
                stack.append((r1.right,r2.right,r.right))
            elif not r2.right :
                r.right=r1.right
            else :
                r.right=r2.right
        return dummy


        
            