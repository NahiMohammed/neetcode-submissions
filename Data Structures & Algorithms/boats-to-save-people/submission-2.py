class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res=0
        people.sort()
        l=0
        r=len(people)-1
        print(people)
        while l<=r :
            print(f"debut l=={l} and  r == {r}")
            if people[r]+people[l]<=limit :
                l+=1
            r-=1
            res+=1

        return res
"""
 3 
0  
1
3
"""