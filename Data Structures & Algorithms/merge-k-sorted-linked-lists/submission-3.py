import heapq

class Solution:
    def mergeKLists(self, lists):
        heap = []
        counter = 0  # avoids comparison issues between nodes

        # 1. Push first node of each list
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, counter, node))
                counter += 1

        dummy = tail = ListNode()

        # 2. Process heap
        while heap:
            _, _, node = heapq.heappop(heap)

            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(heap, (node.next.val, counter, node.next))
                counter += 1

        return dummy.next