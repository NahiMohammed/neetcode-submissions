class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(["a","e","i","o","u"])
        res=  0 
        for i in range(k) :
            if s[i] in  vowels :
                res +=1

        curr = res
        for r in range(k,len(s)) :
            if s[r] in vowels :
                curr+=1
            if s[r-k] in vowels :
                curr-=1

            res = max(res,curr)

        return res
