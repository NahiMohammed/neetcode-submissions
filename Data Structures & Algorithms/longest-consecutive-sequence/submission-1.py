class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums :
            return 0
        s=set(nums)
        res=1
        for n in nums : 
            if n-1 in s :
                continue 
            i=0
            while n+i in s :
                i+=1
            res=max(res,i)
        return res

        