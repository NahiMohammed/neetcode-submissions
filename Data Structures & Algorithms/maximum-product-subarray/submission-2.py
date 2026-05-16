class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_ending = nums[0]
        min_ending = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]

            candidates = (x, max_ending * x, min_ending * x)

            max_ending = max(candidates)
            min_ending = min(candidates)

            result = max(result, max_ending)

        return result
        
        