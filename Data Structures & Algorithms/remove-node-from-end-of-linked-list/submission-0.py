# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length=1
        curr=head
        while curr.next :
            length+=1
            curr=curr.next
        n=length-n+1
        dummy=ListNode(0,head)
        i =1
        curr=dummy
        while i!=n :
            curr=curr.next
            i+=1
            
        curr.next=curr.next.next
        return dummy.next

        