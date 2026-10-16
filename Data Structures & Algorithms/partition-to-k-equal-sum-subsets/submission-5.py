class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums)%k!=0 :
            return False
        sides = [0]*k
        length = sum(nums)//k
        nums.sort(reverse=True)
        if nums[0]>length :
            return False
        def backtracking(i) :
            if i==len(nums) :
                return True

            for j,side in enumerate(sides) :
                if side + nums[i] >length :
                    continue 
                else :
                    sides[j]+=nums[i]
                    if backtracking(i+1) :
                        return True
                    sides[j]-=nums[i]
                if sides[j]==0 :
                    break

            return False



        return backtracking(0)
        

        