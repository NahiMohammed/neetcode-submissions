# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def sortedInsert(sortedHead, current): 

            if sortedHead is None or sortedHead.val >= current.val :
                current.next = sortedHead
                return current

            temp = sortedHead

            while temp.next is not None and temp.next.val < current.val :
                temp = temp.next

            current.next = temp.next
            temp.next = current

            return sortedHead

        current = head
        sortedHead = None

        while current is not None :
            nextNode = current.next
            sortedHead = sortedInsert(sortedHead, current)
            current = nextNode

        return sortedHead