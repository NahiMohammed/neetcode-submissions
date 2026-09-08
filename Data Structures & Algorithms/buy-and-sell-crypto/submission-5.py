class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr=prices[0]
        prof=0
        for p in prices :
            if p<curr :
                curr=p
            else :
                prof=max(prof,p-curr)
        return prof
        