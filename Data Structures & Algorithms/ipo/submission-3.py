class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap_capital = []
        heap_profit = []
        n = len(capital)
        selected = set()
        done = 0
        for i in range(n):
            heapq.heappush(heap_capital, (capital[i], i))
        while heap_capital and heap_capital[0][0] <= w:
            _, idx = heapq.heappop(heap_capital)
            heapq.heappush(heap_profit, (-profits[idx]))

        while done < k and heap_profit:
            pr = heapq.heappop(heap_profit)
            pr = -pr
            w += pr
            while heap_capital and heap_capital[0][0] <= w:
                _, idx = heapq.heappop(heap_capital)
                heapq.heappush(heap_profit, (-profits[idx]))
            done += 1

        return w
