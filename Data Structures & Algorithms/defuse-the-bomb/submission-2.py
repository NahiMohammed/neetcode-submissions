class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res = [0]*len(code)
        n=len(code)
        if k == 0 :
            return res 
        s = 0
        if k>0 :
           
            for i in range(1,k+1): 
                s+=code[i%n]
            res[0] = s
            for i in range(1,len(res)) :
                s+=code[(k+i)%n]
                s-=code[i]
                res[i]= s
        else:
            for i in range(n + k, n):
                s += code[i]

            res[0] = s

            for i in range(1, n):
                s += code[i - 1]
                s -= code[i + k - 1]
                res[i] = s

        return res

