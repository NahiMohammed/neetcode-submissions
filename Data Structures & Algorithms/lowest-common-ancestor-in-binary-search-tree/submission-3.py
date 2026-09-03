# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr =root
        if p.val >q.val :
            p,q=q,p
        while True :
            if curr.val >= p.val and curr.val<=q.val :
                return curr
            elif  curr.val>q.val :
                curr= curr.left 
            else : 
                curr=curr.right
        return None
