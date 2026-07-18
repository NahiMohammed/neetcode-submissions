# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dummy = ListNode()
        tail = dummy

        curr = head
        while curr:
            tail.next = ListNode(curr.val)
            tail = tail.next
            curr = curr.next
        copy = dummy.next

        prev=None
        curr=head
        i=0
        while curr :
            tmp=curr.next
            curr.next=prev
            prev=curr
            curr=tmp
            i+=1

        res=2
        for _ in range(i//2):
            res=max(res,prev.val+copy.val)
            copy=copy.next
            prev=prev.next
        return res

