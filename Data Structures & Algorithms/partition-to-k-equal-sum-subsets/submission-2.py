class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        target = total // k
        used = [False] * len(nums)
        
        def dfs(start, current_sum, sides_done):
            if sides_done == k-1:  # les 3 premiers côtés formés → le 4ème l'est forcément
                return True
            
            if current_sum == target:
                return dfs(0, 0, sides_done + 1)  # on recommence pour le prochain côté
            
            for i in range(start, len(nums)):
                if used[i] or current_sum + nums[i] > target:
                    continue
                used[i] = True
                if dfs(i + 1, current_sum + nums[i], sides_done):
                    return True
                used[i] = False
            
            return False
        
        return dfs(0, 0, 0)
    