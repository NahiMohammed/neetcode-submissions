class Solution:
    def reverseBetween(
        self,
        head: Optional[ListNode],
        left: int,
        right: int
    ) -> Optional[ListNode]:

        def revers(head):
            prev, curr = None, head

            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            return prev

        dummy = ListNode(0)
        dummy.next = head

        # Find the node before `left`
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        # Start of the part to reverse
        start = prev.next

        # Find the node after `right`
        end = start

        for _ in range(right - left):
            end = end.next

        after = end.next

        # Disconnect the part we want to reverse
        end.next = None

        # Reverse it
        reversed_head = revers(start)

        # Connect previous part -> reversed part
        prev.next = reversed_head

        # `start` is now the LAST node after reversal
        start.next = after

        return dummy.next