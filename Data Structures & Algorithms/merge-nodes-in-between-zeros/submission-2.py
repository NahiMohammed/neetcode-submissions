class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = head.next
        node = head
        while node:
            s = node.val
            fast = node.next
            while fast.val != 0:
                s += fast.val
                fast = fast.next
            node.val = s
            node.next = fast.next
            node = node.next
        return head