# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def l(head) :
            res=0 
            while head :
                res+=1
                head=head.next
            return res
        n = l(head)-n
        if n ==0 :
            return head.next
        cur = 0
        curr = head
        while True :
            if cur+1 == n :
                curr.next =curr.next.next
                return head
            cur+=1
            curr=curr.next

        return head

        