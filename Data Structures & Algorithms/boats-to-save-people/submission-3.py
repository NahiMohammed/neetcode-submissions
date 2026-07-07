class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res=0
        l=0
        r=len(people)-1
        print(f"people{people}")
        while l<=r :
            sum=people[r]
            r-=1
            
            if sum+people[l]<=limit :
                sum+=people[l]
                l+=1
            res+=1
            print(f"une fois r: {r} l:{l}")
        return res
        