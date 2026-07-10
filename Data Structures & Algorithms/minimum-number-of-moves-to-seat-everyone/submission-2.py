class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        max_index=max(max(seats),max(students))+1
        a=[0]*max_index
        b=[0]*max_index
        for seat in seats :
            a[seat]+=1
        for student in students :
            b[student]+=1
        remain =len(seats)
        i=0
        j=0
        res=0
        while remain :
            if a[i]==0:
                i+=1
            if b[j]==0:
                j+=1
            if a[i] and b[j] :
                res+=abs(i-j)
                a[i]-=1
                b[j]-=1
                remain-=1
        return res

        