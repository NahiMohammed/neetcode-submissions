# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res= [] 
        curr =head 
        while curr  :
            res.append(curr.val )
            curr= curr.next
        return max(res[i] + res[len(res)-1-i] for i in range(len(res)//2))    