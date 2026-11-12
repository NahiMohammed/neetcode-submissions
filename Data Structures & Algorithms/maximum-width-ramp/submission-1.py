class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        st = []
        for i, n in enumerate(nums):
            if not st or nums[st[-1]] > n:
                st.append(i)

        ans = 0
        for j in reversed(range(len(nums))):
            while st and nums[st[-1]] <= nums[j]:
                ans = max(ans, j - st.pop())
        return ans