class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(k):
            if k < 0:
                return 0
            l = s = res = 0
            for r in range(len(nums)):
                s += nums[r]
                while s > k:
                    s -= nums[l]
                    l += 1
                res += r - l + 1
            return res

        return atMost(goal) - atMost(goal - 1)
        