# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root :
            return 0
        stack=[root]
        l=[1]
        res=1
        while stack :
            curr=stack.pop()
            length=l.pop()
            if curr.left :
                stack.append(curr.left)
                l.append(length+1)
                res=max(length+1,res)
            if curr.right :
                stack.append(curr.right)
                l.append(length+1)
                res=max(length+1,res)
        return res

         
        