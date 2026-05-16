class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[-1] = True

        for i in range(n-2, -1, -1):
            far = min(n-1, i + nums[i])
            for j in range(i+1, far+1):
                if dp[j]:
                    dp[i] = True
                    break

        return dp[0]