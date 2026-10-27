class Solution:
    def compress(self, chars: List[str]) -> int:
        res=[]
        i = 0 
        while i<len(chars) :
            c = chars[i]
            j=i+1
            while j<len(chars) and  chars[j]==chars[i] :
                j+=1
            res.append(c)
            if j-i>1 :

                res.extend(list(str(j-i)))
            i=j
        print(res)
        for i in range(len(res)): 
            chars[i] = res[i]
        return len(res)
            