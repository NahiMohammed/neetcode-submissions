class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res=""
        occ={}
        for i in range(len(t)):
            occ[t[i]]=occ.get(t[i],0)+1

        for i in range(len(s)):
            if s[i]  in occ:
                j=i
                occ2={}
                occ2[s[i]]=occ2.get(s[i],0)+1
                while j<len(s)-1 and not all(occ2.get(c, 0)>= occ[c] for c in occ):
                    j+=1
                    if s[j] in occ:
                        occ2[s[j]]=occ2.get(s[j],0)+1
                if j>=len(s):
                    return res
                if all(occ2.get(c, 0)>= occ[c] for c in occ):
                    if res=="" or j-i<len(res):
                        res=s[i:j+1]
                
                    


        return res



