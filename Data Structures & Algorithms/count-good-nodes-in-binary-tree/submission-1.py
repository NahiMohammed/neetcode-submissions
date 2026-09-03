# Definition for a binary tree node.
# class TreeNode:
#     def __init__(Deque, self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q=deque([(root,root.val)])
        res=0
        while q :

            node , m = q.popleft()
            if node.val>=m :
                res+=1
            if node.left :
                q.append((node.left ,max(m,node.left.val)))
            if node.right :
                q.append((node.right,max(m,node.right.val)))
        return res







        