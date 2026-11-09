class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        res= 0
        for i in range(len(customers)) :
            if grumpy[i]==0 :
                res+=customers[i]
        original = res 
        curr = 0
        for i in range(minutes):
            if grumpy[i]==1 :
                curr+=customers[i]
        res = max( res , original+curr)
        for i in range(minutes , len(grumpy)) :
            if grumpy[i-minutes] == 1 :
                curr-=customers[i-minutes]
            if grumpy[i]==1 :
                curr+=customers[i]
            res = max( res , original+curr)
        return res
            
        
        