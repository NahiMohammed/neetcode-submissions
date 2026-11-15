# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self, list1: Optional[ListNode], a: int, b: int, list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, list1)
        curr= dummy 
        while a  :
            curr=curr.next
            a-=1
        firstend = curr
        curr = list1
        while b :
            curr = curr.next 
            b-=1
        curr = curr.next 
        secondhalf = curr
        firstend.next  = list2 
        curr = list2 
        while curr.next :
            curr=curr.next 

        curr.next = secondhalf 
        return dummy.next

 
