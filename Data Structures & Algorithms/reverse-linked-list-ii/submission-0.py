class Solution:
    def reverseBetween(
        self,
        head: Optional[ListNode],
        left: int,
        right: int
    ) -> Optional[ListNode]:

        def reverse(head):
            prev = None
            curr = head

            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            return prev

        dummy = ListNode(0)
        dummy.next = head

        # Find the node BEFORE left
        before = dummy

        for _ in range(left - 1):
            before = before.next

        # Find the node AFTER right
        after = before.next

        for _ in range(right - left + 1):
            after = after.next

        # Save the beginning of the part to reverse
        start = before.next

        # Disconnect the part
        before.next = None
        start.next = None

        # Reverse [left, right]
        reversed_head = reverse(start)

        # Find the end of the reversed list
        reversed_tail = reversed_head

        while reversed_tail.next:
            reversed_tail = reversed_tail.next

        # Reconnect
        before.next = reversed_head
        reversed_tail.next = after

        return dummy.next