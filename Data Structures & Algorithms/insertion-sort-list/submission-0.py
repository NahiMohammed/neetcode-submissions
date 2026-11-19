# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)          # head of the sorted list
        cur = head

        while cur:
            nxt = cur.next           # save it, because we will change cur.next

            # second loop: start from the head (dummy) each time
            prev = dummy
            while prev.next and prev.next.val < cur.val:
                prev = prev.next

            # insert cur between prev and prev.next
            cur.next = prev.next
            prev.next = cur

            cur = nxt

        return dummy.next