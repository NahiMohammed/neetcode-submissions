class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        res = []
        perm = []
        pick = [False] * len(nums)

        def backtrack():
            if len(perm) == len(nums):
                res.append(perm[:])
                return

            for i in range(len(nums)):
                if pick[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not pick[i-1]:
                    continue

                perm.append(nums[i])
                pick[i] = True

                backtrack()

                perm.pop()
                pick[i] = False

        backtrack()
        return res