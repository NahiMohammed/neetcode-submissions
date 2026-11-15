# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        n = 0
        first_critcal = -1 
        last_critical = -1 
        res= [-1,-1]
        prev = head.val 

        curr = head.next

        while curr and curr.next :
            n+=1 
            if (curr.val>curr.next.val and curr.val>prev )  or (curr.val<curr.next.val and curr.val<prev ) :
                 
                if first_critcal == -1 :
                    first_critcal = n
                    last_critical = n
                    
                else : 
                    if res ==[-1,-1] :
                        res = [n - last_critical, n - first_critcal]
                    else :
                        res[0] = min(res[0], n - last_critical)
                        res[1] = n - first_critcal
                    last_critical = n
            prev =curr.val 
            curr= curr.next
        return res


        