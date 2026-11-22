class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        def check(head, node) :
            # the list is finished: every value matched
            if not head:
                return True
            # the tree path ended, or the values are different
            if not node or node.val != head.val:
                return False
            # go down: left or right child, next list node
            return check(head.next, node.left) or check(head.next, node.right)
        
        if not root:
            return False
        q = deque([root])
        while q  :
            node = q.popleft()
            if node.val ==head.val :
                if check(head,node) :
                    return True
            if node.left :
                q.append(node.left)
            if node.right :
                q.append(node.right)
        return False

