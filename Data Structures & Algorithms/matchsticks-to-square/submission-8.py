class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        s = sum(matchsticks)
        if s % 4 != 0:
            return False
        target = s // 4
        used = [False] * len(matchsticks)
        matchsticks.sort(reverse=True)
        def backtracking(n, curr):
            
            if n == 4:
                return True
            for i, match in enumerate(matchsticks):
                if used[i]:
                    continue
                if curr + match > target:
                    continue

                used[i] = True

                if curr + match == target:
                    if backtracking(n + 1, 0):
                        return True
                else:
                    if backtracking(n, curr + match):
                        return True

                used[i] = False

            return False

        return backtracking(0, 0)