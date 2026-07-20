class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        s = sum(matchsticks)

        if s % 4 != 0:
            return False

        target = s // 4

        matchsticks.sort(reverse=True)
        if matchsticks[0] > target:
            return False

        n = len(matchsticks)
        used = [False] * n

        def backtracking(curr, sides):
            if sides == 3:
                return True
            if curr == target:
                return backtracking(0, sides + 1)

            prev = -1

            for i in range(n):

                if used[i]:
                    continue

                # Évite les doublons
                if matchsticks[i] == prev:
                    continue

                if curr + matchsticks[i] > target:
                    continue

                prev = matchsticks[i]

                used[i] = True

                if backtracking(curr + matchsticks[i], sides):
                    return True

                used[i] = False

            return False

        return backtracking(0, 0)