from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        
        target = s // 2
        dp = set([0])
        
        for num in nums:
            new_dp = set(dp)
            for x in dp:
                if x + num == target:
                    return True
                new_dp.add(x + num)
            dp = new_dp
        
        return target in dp