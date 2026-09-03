# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        cur=root
        done=False
        if not cur :
            return TreeNode(val)
        while not done : 
            if val <cur.val:
                if not cur.left :
                    cur.left = TreeNode(val)
                    done =True
                else :

                    cur=cur.left 
            else :
                if not cur.right:
                    cur.right = TreeNode(val)
                    done =True
                else :
                    cur=cur.right

                    
            

        return root
