# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(root) :
            if not root :
                 return 0 
            return 1 + max(depth(root.left),depth(root.right))
        if not root :
            return True 
        stack = [root] 
        while stack :
            curr=stack.pop()
            if abs(depth(curr.left)-depth(curr.right))>1 :
                return False 
            if curr.left :
                stack.append(curr.left) 
            if curr.right :
                stack.append(curr.right)
        return True
        