class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        if not root :
            return res
        q=deque([root])
        curr=root
        while q :
            res.append(q[-1].val)
            for i in range(len(q)):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right :
                    q.append(node.right)



        return res
