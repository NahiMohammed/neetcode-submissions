# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(head):
            prev = None
            curr = head

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            return prev

        # Reverse the list
        head = reverse(head)

        # Remove nodes smaller than the maximum seen so far
        mx = head.val
        curr = head

        while curr and curr.next:
            if curr.next.val < mx:
                curr.next = curr.next.next
            else:
                curr = curr.next
                mx = curr.val

        # Reverse back
        return reverse(head)