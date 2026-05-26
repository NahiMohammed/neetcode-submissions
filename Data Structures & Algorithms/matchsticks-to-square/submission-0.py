class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        
        target = total // 4
        used = [False] * len(matchsticks)
        
        def dfs(start, current_sum, sides_done):
            if sides_done == 3:  # les 3 premiers côtés formés → le 4ème l'est forcément
                return True
            
            if current_sum == target:
                return dfs(0, 0, sides_done + 1)  # on recommence pour le prochain côté
            
            for i in range(start, len(matchsticks)):
                if used[i] or current_sum + matchsticks[i] > target:
                    continue
                used[i] = True
                if dfs(i + 1, current_sum + matchsticks[i], sides_done):
                    return True
                used[i] = False
            
            return False
        
        return dfs(0, 0, 0)