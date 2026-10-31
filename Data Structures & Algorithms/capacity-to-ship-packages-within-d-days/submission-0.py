class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def condition(capacity) :
            total =0 
            total_days = 1
            for w in weights :
                total+=w 
                if total>capacity :
                    total = w
                    total_days+=1
                    if total_days>days :
                        return False
            return True

        l = max(weights)
        r = sum(weights)
        while l<r :
            mid = l+ (r-l)//2
            if condition(mid):
                r=mid
            else :
                l=mid+1
        return l
        