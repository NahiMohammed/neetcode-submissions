class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def compare(w1,w2):
            l=0
            while (l<min(len(w1),len(w2))) :
                if (dic[w1[l]]==dic[w2[l]]):
                    l+=1
                elif (dic[w1[l]]>dic[w2[l]]):
                    return 0
                else :
                    return 1
                
            if len(w2)<len(w1):
                return 0
            else :
                return 1


        dic={}
        for i in range(len(order)):
            dic[order[i]]=i
        for i in range(len(words)-1):
            if compare(words[i],words[i+1])==0 :
                print(f"words[i] {words[i]}")
                print(f"words[i+1] {words[i+1]}")
                return False
        return True