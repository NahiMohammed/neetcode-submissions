class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        res=0
        students.sort()
        seats.sort()
        for i in range(len(seats)):
            if seats[i]!=students[i]:
                res+=abs(students[i]-seats[i])
        return res
