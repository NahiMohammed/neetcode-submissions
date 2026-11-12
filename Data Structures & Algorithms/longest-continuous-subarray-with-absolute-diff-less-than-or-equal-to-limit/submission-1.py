from collections import deque
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxd = deque()   # indices, values decreasing, front = max
        mind = deque()   # indices, values increasing, front = min
        left = 0
        res = 0
        for right, x in enumerate(nums):
            while maxd and nums[maxd[-1]]<x :
                maxd.pop()
            maxd.append(right)
            while mind and nums[mind[-1]]>x :
                mind.pop()
            mind.append(right)

            while nums[maxd[0]] - nums[mind[0]] > limit:
                left += 1
                if maxd[0] < left:
                    maxd.popleft()
                if mind[0] < left:
                    mind.popleft()

            res = max(res, right - left + 1)
        return res