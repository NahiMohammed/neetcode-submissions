class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        lowest_price=prices[0]
        for i , p in enumerate(prices):
            res=max(res,p-lowest_price)
            if p<lowest_price :
                lowest_price
            

        return res


        