class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        s = sum(matchsticks)

        if s % 4 != 0:
            return False

        target = s // 4

        # Très important : essayer les grandes allumettes d'abord
        matchsticks.sort(reverse=True)

        used = [False] * len(matchsticks)

        def backtracking(curr, sides):
            # 3 côtés sont terminés => le 4e est forcément correct
            if sides == 3:
                return True

            # Un côté est terminé, on commence le suivant
            if curr == target:
                return backtracking(0, sides + 1)

            for i in range(len(matchsticks)):
                if used[i]:
                    continue

                if curr + matchsticks[i] > target:
                    continue

                used[i] = True

                if backtracking(curr + matchsticks[i], sides):
                    return True

                used[i] = False

            return False

        return backtracking(0, 0)