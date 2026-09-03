class Solution:
    def checkValidString(self, s: str) -> bool:
        open=0
        closed=0
        joker=0
        for c in s :
            if c=="*" :
                joker+=1
            elif c=="(" :
                open+=1 
            else :
                if open==0 :
                    if joker ==0 :
                        return False
                    else :
                        joker-=1
                else :
                    open-=1
        return joker>=open

        