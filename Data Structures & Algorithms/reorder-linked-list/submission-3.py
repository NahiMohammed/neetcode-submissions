class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        def reverse(head):
            prev = None
            curr = head

            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            return prev

        # Find middle
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Split
        list2 = slow.next
        slow.next = None

        # Reverse second half
        list2 = reverse(list2)

        # Merge
        list1 = head

        while list2:
            tmp1 = list1.next
            tmp2 = list2.next

            list1.next = list2
            list2.next = tmp1

            list1 = tmp1
            list2 = tmp2