class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ord={}
        for i in range(len(order)):
            ord[order[i]]=i
        def compare(w1,w2) :

            i=0
            while i<min(len(w1),len(w2)) and ord[w2[i]]==ord[w1[i]]:
                i+=1
            print(i)
            if i<min(len(w1),len(w2)) :
                if ord[w2[i]]< ord[w1[i]] :
                    return False
                else: 
                    return True
            else :
                if len(w1)>len(w2) :
                    return False
                else :
                    return True

        for i in range(1,len(words)) :
            if not compare(words[i-1],words[i]) :
                print(words[i],words[i-1])
                return False
        return True
