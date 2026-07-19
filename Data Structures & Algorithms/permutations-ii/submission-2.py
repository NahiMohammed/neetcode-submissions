class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        nums.sort()  # so duplicates sit next to each other
        self.backtrack([], nums, [False] * len(nums))
        return self.res

    def backtrack(self, perm: List[int], nums: List[int], pick: List[bool]):
        if len(perm) == len(nums):
            self.res.append(perm[:])
            return
        for i in range(len(nums)):
            if pick[i]:
                continue
  
            if i > 0 and nums[i] == nums[i - 1] and not pick[i - 1]:
                continue
            perm.append(nums[i])
            pick[i] = True
            self.backtrack(perm, nums, pick)
            perm.pop()
            pick[i] = False