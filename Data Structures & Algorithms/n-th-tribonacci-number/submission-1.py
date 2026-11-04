class Solution:
    def tribonacci(self, n: int) -> int:
        t=[0,1,1]
        if n<=2 :
            return t[n]

        while n>2 :
            tmp = t[0]+t[-1]+t[1]
            t[0]=t[1]
            t[1]=t[2]
            t[2]=tmp
            n-=1
        return t[-1]
        