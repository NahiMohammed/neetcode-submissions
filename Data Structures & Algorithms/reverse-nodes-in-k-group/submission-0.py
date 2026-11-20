class Solution:
    def reverseKGroup(self, head, k):

        def reverseK(head):
            prev = None
            curr = head

            for _ in range(k):
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            head.next = curr
            return prev

        n = 0
        curr = head

        while curr:
            n += 1
            curr = curr.next

        number_of_groups = n // k

        dummy = ListNode(0, head)
        prev_group_tail = dummy
        curr = head

        for _ in range(number_of_groups):
            new_head = reverseK(curr)

            prev_group_tail.next = new_head
            prev_group_tail = curr
            curr = curr.next

        return dummy.next