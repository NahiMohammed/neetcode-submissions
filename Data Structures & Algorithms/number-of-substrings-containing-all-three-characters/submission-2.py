class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0 
        res= 0 
        n = len(s)
        dic = defaultdict(deque)
        for r in range(n) :
            dic[s[r]].append(r)
            while len(dic)==3 :
                res+=n-r
                c = s[l]
                dic[c].popleft()
                l+=1
                if not dic[c] :
                    del dic[c]
        return res

