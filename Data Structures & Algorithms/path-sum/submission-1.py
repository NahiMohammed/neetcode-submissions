# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root :
            return False
        cur_sum = root.val
        stack=[[root,cur_sum]]
        while stack :
            n ,s = stack.pop()
            if not n.left and not n.right :
                if s==targetSum :
                    return True
            else :

                if n.left :
                    stack.append([n.left , s+n.left.val])
                if n.right : 
                    stack.append([n.right , s+n.right.val])
        return False

            


        