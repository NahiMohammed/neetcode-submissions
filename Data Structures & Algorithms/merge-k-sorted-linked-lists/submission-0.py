# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = []
        for i in range(len(lists)) :
            curr = lists[i]
            while curr :
                l.append(curr.val)
                curr=curr.next

        dummy = ListNode(0)
        curr = dummy
        for n in sorted(l) :
            curr.next = ListNode(n) 
            curr=curr.next
        return dummy.next   