class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic={}
        for i , c in enumerate(order) :
            dic[c]= i 

        def compare(w1,w2):
            n = min(len(w1),len(w2))
            flag= False
            for i in range(n) :

                if dic[w1[i]]<dic[w2[i]] :
                    return True
                if dic[w2[i]]<dic[w1[i]] :
                    return False
            return len(w1)<=len(w2)
        for i in range(1,len(words)) :
            if not compare(words[i-1],words[i]) :
                return False
        return True
        