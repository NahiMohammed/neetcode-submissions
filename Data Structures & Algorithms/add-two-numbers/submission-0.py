# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        a=0
        curr1=l1
        while curr1 and l2 :
            val1=curr1.val
            val2=l2.val

            val=val1+val2+a
            print(val)
            curr1.val=val%10

            a=val//10
            print(a)
            curr1=curr1.next
            l2=l2.next
        if a :
            l1.next=ListNode(1)
        return l1












    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        