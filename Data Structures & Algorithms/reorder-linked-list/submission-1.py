class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev_val = head.val
        curr = head.next
        pos = 2

        first = -1
        prev_critical = -1
        min_dist = float("inf")

        while curr and curr.next:
            if (curr.val > prev_val and curr.val > curr.next.val) or \
               (curr.val < prev_val and curr.val < curr.next.val):

                if first == -1:
                    first = pos
                else:
                    min_dist = min(min_dist, pos - prev_critical)

                prev_critical = pos

            prev_val = curr.val
            curr = curr.next
            pos += 1

        if first == -1 or first == prev_critical:
            return [-1, -1]

        return [min_dist, prev_critical - first]