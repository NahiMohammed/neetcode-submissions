class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode(0)
        more = ListNode(0)
        l, m = less, more
        curr = head
        while curr:
            if curr.val < x:
                l.next = curr
                l = l.next
            else:
                m.next = curr
                m = m.next
            curr = curr.next

        m.next = None      # cut the tail, otherwise you may create a cycle
        l.next = more.next
        return less.next