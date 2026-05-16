class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            x = nums[i]
            candidates = (x, current + x)

            current = max(candidates)

            result = max(result, current)

        return result
        
        