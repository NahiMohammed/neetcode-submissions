class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = cur_min = res = nums[0]
        for x in nums[1:]:
            candidates = (x, x * cur_max, x * cur_min)
            cur_max, cur_min = max(candidates), min(candidates)
            res = max(res, cur_max)
        return res