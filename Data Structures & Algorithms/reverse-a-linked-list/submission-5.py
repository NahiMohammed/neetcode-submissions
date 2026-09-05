# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list=[]
        curr= head 
        while curr :
            list.append(curr.val) 
            curr=curr.next
        list.reverse()
        curr=head
        for i in range(len(list)) :
            curr.val=list[i]
            curr=curr.next
        return head


        