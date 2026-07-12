class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        head = res

        head1 = list1
        head2 = list2

        if not head1:
            return head2
        if not head2:
            return head1

        while head1 and head2:
            if head1.val < head2.val:
                res.val = head1.val
                head1 = head1.next
            else:
                res.val = head2.val
                head2 = head2.next

            if head1 or head2:
                res.next = ListNode()
                res = res.next

        while head1:
            res.val = head1.val
            head1 = head1.next
            if head1:
                res.next = ListNode()
                res = res.next

        while head2:
            res.val = head2.val
            head2 = head2.next
            if head2:
                res.next = ListNode()
                res = res.next

        return head