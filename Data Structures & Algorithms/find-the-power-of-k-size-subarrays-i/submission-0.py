class Solution:
    def resultsArray(self, nums, k):
        res = []
        run = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1] + 1:
                run += 1
            else:
                run = 1
            if i >= k - 1:
                res.append(nums[i] if run >= k else -1)
        return res