# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def length(head):
            count = 0
            current = head

            while current:
                count += 1
                current = current.next

            return count

        if length(l1)<length(l2):
            l1,l2=l2,l1
        
        dummy = node = ListNode()
        a=0
        curr1=l1
        while curr1 or  l2 :
            val1=curr1.val
            if not l2 :
                val2=0
            else :
                
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
        