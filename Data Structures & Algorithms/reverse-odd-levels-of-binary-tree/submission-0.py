# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root :
            return root
        level =  0 
        q = deque([root]) 
        st = [root.val]
        while q :
            n = len(q)
            if level%2 == 1 :
                for i in range(n // 2):
                    q[i].val, q[n-1-i].val = q[n-1-i].val, q[i].val
            for i in range(len(q)) :
                n = q.popleft()
                if n.left :
                    q.append(n.left)
                if n.right :
                    q.append(n.right)
            level+=1
        return root

        