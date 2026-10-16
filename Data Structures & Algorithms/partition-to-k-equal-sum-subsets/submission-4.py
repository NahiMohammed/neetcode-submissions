
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False

        target = sum(nums) // k
        nums.sort(reverse=True)

        if nums[0] > target:
            return False

        sides = [0] * k

        def backtracking(i):
            if i == len(nums):
                return True

            for j in range(k):
                if sides[j] + nums[i] > target:
                    continue

                sides[j] += nums[i]

                if backtracking(i + 1):
                    return True

                sides[j] -= nums[i]

                # Don't try other equivalent empty sides
                if sides[j] == 0:
                    break

            return False

        return backtracking(0)
