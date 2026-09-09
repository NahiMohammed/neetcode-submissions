class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        s = sum(matchsticks)

        if s % 4 != 0:
            return False

        target = s // 4

        matchsticks.sort(reverse=True)

        # Important: impossible immediately
        if matchsticks[0] > target:
            return False

        used = [False] * len(matchsticks)

        def backtracking(n, curr):
            if n == 4:
                return True

            for i, match in enumerate(matchsticks):

                if used[i]:
                    continue

                if curr + match > target:
                    continue

                # Avoid trying identical sticks at the same position
                if i > 0 and matchsticks[i] == matchsticks[i - 1] and not used[i - 1]:
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