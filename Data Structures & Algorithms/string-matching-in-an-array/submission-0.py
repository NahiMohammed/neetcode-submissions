class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        def sub(a,b):
            if len(a)>len(b):
                return False
            for i in range(len(b)-len(a)+1):
                if a[0]==b[i]:
                    if b[i:i+len(a)]==a :
                        return True
            return False
        res=set()

        for i in range(len(words)) :
            for j in range(len(words)):
                if j==i:
                    continue
                if sub(words[i],words[j]):
                    print(f" {words[i]},{words[j]}")

                    res.add(words[i])
        return list(res)


        