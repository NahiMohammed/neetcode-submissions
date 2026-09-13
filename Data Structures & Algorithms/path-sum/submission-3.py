# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        res=[]
        curr_path=[]
        def dfs(node, curr_sum) :
            if not node :
                return 
            curr_sum+=node.val
            curr_path.append(node.val)

            if curr_sum ==targetSum and not node.left and not node.right:
                res.append(curr_path.copy())
                 
            if node.left :
                dfs(node.left,curr_sum)

            if node.right :
                dfs(node.right,curr_sum)
            curr_path.pop()
        dfs(root,0)
        return len(res)>0
        