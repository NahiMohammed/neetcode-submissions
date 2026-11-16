# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res = []
        n = 0 
        curr = head 
        while curr :
            n+=1
            curr = curr.next 
        length = n//k 
        left = n % k 
        for _ in range(k):
            curr = head
            if curr:
                size = length + (1 if left > 0 else 0)
                if left > 0:
                    left -= 1
                for _ in range(1, size):
                    curr = curr.next
                tmp = curr.next
                curr.next = None
                res.append(head)
                head = tmp
            else:
                res.append(None)
        return res

        