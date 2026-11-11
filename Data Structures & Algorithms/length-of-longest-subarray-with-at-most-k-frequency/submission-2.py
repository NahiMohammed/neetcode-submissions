from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums, k):
        count = defaultdict(int)
        l = res = 0
        for r, x in enumerate(nums):
            count[x] += 1
            while count[x] > k:
                count[nums[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res