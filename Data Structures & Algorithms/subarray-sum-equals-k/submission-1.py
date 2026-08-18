class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            s = 0
            j = i
            while j < len(nums):
                s += nums[j]
                j += 1

                if s == k:
                    res += 1

        return res
