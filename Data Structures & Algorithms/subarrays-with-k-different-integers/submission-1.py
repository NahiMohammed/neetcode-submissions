class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def at_most(k):
            count = defaultdict(int)
            left = res = 0
            for right, x in enumerate(nums):
                count[x] += 1
                while len(count) > k:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    left += 1
                res += right - left + 1
            return res

        return at_most(k) - at_most(k - 1)