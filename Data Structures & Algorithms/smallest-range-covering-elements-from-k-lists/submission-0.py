import heapq
class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        left = nums[0][0]
        right = nums[0][0]
        min_heap =  []
        for i , row in enumerate(nums) :
            left = min(left,row[0])
            right = max(right,row[0])
            heapq.heappush(min_heap, (row[0], i , 0))

        res = [left , right] 
        while True:
            l, i, idx = heapq.heappop(min_heap)
            idx += 1

            if idx >= len(nums[i]):
                return res

            right = max(right, nums[i][idx])
            heapq.heappush(min_heap, (nums[i][idx], i, idx))

            left = min_heap[0][0]

            if right - left < res[1] - res[0]:
                res = [left, right]
            