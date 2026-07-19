class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subset = []

        def backtrack(start, total):
            if total == target:
                res.append(subset.copy())
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates at the same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since the array is sorted, no need to continue
                

                subset.append(candidates[i])
                backtrack(i + 1, total + candidates[i])  # i+1 because each number can only be used once
                subset.pop()

        backtrack(0, 0)
        return res