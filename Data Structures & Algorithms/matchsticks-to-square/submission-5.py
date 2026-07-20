class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        s = sum(matchsticks)

        if s % 4 != 0:
            return False

        target = s // 4

        # Les grandes allumettes d'abord
        matchsticks.sort(reverse=True)

        # Si la plus grande dépasse déjà le côté
        if matchsticks[0] > target:
            return False

        sides = [0, 0, 0, 0]

        def backtrack(i):
            if i == len(matchsticks):
                return True

            for j in range(4):

                if sides[j] + matchsticks[i] <= target:
                    sides[j] += matchsticks[i]

                    if backtrack(i + 1):
                        return True

                    sides[j] -= matchsticks[i]

                # Évite de tester plusieurs côtés identiques
                if sides[j] == 0:
                    break

            return False

        return backtrack(0)