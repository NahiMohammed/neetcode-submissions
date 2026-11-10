class Solution:
    def maximumSubarraySum(self, nums, k):
        s = 0
        res = 0
        l = 0
        se = {}
        for r in range(len(nums)):
            s += nums[r]
            se[nums[r]] = r
            if r - l + 1 > k:
                s -= nums[l]
                if se[nums[l]] == l:
                    del se[nums[l]]
                l += 1
            if r - l + 1 == k and len(se) == k:
                res = max(res, s)
        return res