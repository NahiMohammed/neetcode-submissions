# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        curr=dummy 
        curr1 = head.next
        s = 0
        while curr1  :
            if curr1.val == 0 :
                curr.next = ListNode(s)
                curr = curr.next
                s = 0 

            else :
                s+=curr1.val
            curr1 = curr1.next

        return dummy.next 

        