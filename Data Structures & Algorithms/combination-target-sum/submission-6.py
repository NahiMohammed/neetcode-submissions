class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i, total):
            # Found a valid combination
            if total == target:
                res.append(subset.copy())
                return

            # Invalid state
            if i == len(candidates) or total > target:
                return

            # Choice 1: Take candidates[i]
            subset.append(candidates[i])
            backtrack(i, total + candidates[i])  # stay at i (can reuse)
            subset.pop()

            # Choice 2: Skip candidates[i]
            backtrack(i + 1, total)

        backtrack(0, 0)
        return res