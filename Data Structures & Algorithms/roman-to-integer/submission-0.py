class Solution:
    def romanToInt(self, s: str) -> int:
        dic={}
        dic["I"]=1
        dic["V"]=5
        dic["X"]=10
        dic["L"]=50
        dic["C"]=100
        dic["D"]=500
        dic["M"]=1000
        res=0
        i=0
        while i<len(s)-1:
            if dic[s[i]]<dic[s[i+1]]:    
                res+=dic[s[i+1]]-dic[s[i]]
                i+=2
            else :
                res+=dic[s[i]]
                i+=1
        if i==len(s)-1:
            res+=dic[s[i]]
        return res



