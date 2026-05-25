class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        print(nums)

        def dfs(subset , start ):
            print(res)
            res.append(subset.copy())
            for i in range(start,len(nums)):

                
                if i>start and nums[i]==nums[i-1] :
                    continue
                subset.append(nums[i])
                dfs(subset,i+1)
                subset.pop()
        dfs([],0)
        return res


        