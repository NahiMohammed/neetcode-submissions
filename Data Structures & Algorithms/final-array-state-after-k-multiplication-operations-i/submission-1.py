class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []

        # build heap: (value, index)
        for i, val in enumerate(nums):
            heapq.heappush(heap, (val, i))

        for _ in range(k):
            val, i = heapq.heappop(heap)

            val *= multiplier
            nums[i] = val

            heapq.heappush(heap, (val, i))

        return nums