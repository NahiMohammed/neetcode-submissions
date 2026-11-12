class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        vals = sorted(set(nums))
        best = 0
        j = 0
        for i in range(len(vals)):
            while vals[i] - vals[j] >= n:
                j += 1
            best = max(best, i - j + 1)
        return n - best
