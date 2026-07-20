class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        s = sum(matchsticks)

        if s % 4 != 0:
            return False

        target = s // 4

        # Optimisation 1 : trier du plus grand au plus petit
        matchsticks.sort(reverse=True)

        # Optimisation 2 : impossible si une allumette est trop grande
        if matchsticks[0] > target:
            return False

        n = len(matchsticks)
        used = [False] * n

        def backtracking(curr, sides):
            # Si 3 côtés sont construits, le 4e l'est forcément
            if sides == 3:
                return True

            # Côté terminé, on passe au suivant
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