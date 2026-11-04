
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i, flag):
            if (i, flag) in memo:
                return memo[(i, flag)]

            if i == len(nums) - 1:
                res = max(0, nums[i]) if flag else nums[i]
            elif flag:
                res = max(0, nums[i] + dfs(i + 1, True))
            else:
                res = max(
                    dfs(i + 1, False),
                    nums[i] + dfs(i + 1, True)
                )

            memo[(i, flag)] = res
            return res

        return dfs(0, False)
