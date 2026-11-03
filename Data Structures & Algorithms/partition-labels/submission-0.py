class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic ={}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = [i, i]
            else:
                dic[s[i]][1] = i
        i= 0
        res= []
        while i<len(s) :
            
            c=s[i]
            ensemble=set(c)

            right , left = dic[c]
            j = right+1
            while j<=left :
                if s[j] not in ensemble :
                    ensemble.add(s[j])
                    left = max(left,dic[s[j]][1])
                j+=1
            res.append(left-right+1)
            i=left +1 
        return res



            