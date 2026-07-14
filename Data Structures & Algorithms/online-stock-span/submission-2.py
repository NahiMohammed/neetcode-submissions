class StockSpanner:

    def __init__(self):
        self.stack=[]

    def next(self, price: int) -> int:
        res=1
        self.stack.append(price)
        while len(self.stack)>res and self.stack[-1-res]<=price :
            res+=1
        return res

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)