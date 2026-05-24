from functools import reduce

class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None

        def merge(l1, l2):
            dummy = node = ListNode()
            while l1 and l2:
                if l1.val < l2.val:
                    node.next = l1
                    l1 = l1.next
                else:
                    node.next = l2
                    l2 = l2.next
                node = node.next
            node.next = l1 or l2
            return dummy.next

        return reduce(merge, lists)