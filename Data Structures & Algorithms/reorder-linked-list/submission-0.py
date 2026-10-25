# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self,head : Optional[ListNode]) -> Optional[ListNode] :
        prev = None 
        curr = head
        while curr :
            tmp = curr.next
            curr.next = prev
            prev = curr 
            curr = tmp
        return prev

    
    def reorderList(self, head: Optional[ListNode]) -> None:
        def prin(head) :
            res=[]
            while head :
                res.append(head.val)
                head=head.next
            return res
        
        slow = head 
        fast = head 
        while fast.next and fast.next.next :
            slow = slow.next
            fast = fast.next.next
        
        secon_half = slow.next
        slow.next= None

        secon_half = self.reverse(secon_half)


        while secon_half :
            tmp1 ,tmp2 = head.next , secon_half.next
            head.next = secon_half 
            secon_half.next = tmp1 
            head = tmp1
            secon_half = tmp2