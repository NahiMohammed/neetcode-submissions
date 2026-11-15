# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        def build_list(values):
            dummy = ListNode(0)
            cur = dummy
            for v in values:
                cur.next = ListNode(v)
                cur = cur.next
            return dummy.next
        res= []
        curr = head 
        while curr :
            res.append(curr.val)
            curr= curr.next 
        s= sum(1 for i in range(len(res))  if res[i]<x) 
        copy = res.copy()
        i = 0 
        j = s
        for k in range(len(res)) :
            if res[k]<x :
                copy[i]=res[k]
                i+=1
            else :
                copy[j] = res[k]
                j+=1
        print(copy)
        return build_list(copy)