class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(i, xor):
            if i == len(nums):
                return xor

            # Include nums[i]
            include = backtrack(i + 1, xor ^ nums[i])

            # Exclude nums[i]
            exclude = backtrack(i + 1, xor)

            return include + exclude

        return backtrack(0, 0)