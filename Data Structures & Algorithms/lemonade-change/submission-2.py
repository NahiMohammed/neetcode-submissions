class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        wallet={5:0,
        10 : 0,
        20 : 0}
        for b in bills :
            print(b)
            if b == 5 :
                wallet[5]+=1
            elif b==10 :
                if wallet[5]==0 :
                    return False 
                else :
                    wallet[5]-=1
                    wallet[10]+=1
            else :
                if wallet[10]==0 :
                    if wallet[5]<3 :
                        return False
                    else :
                        wallet[5]-=3
                else :
                    if wallet[5]==0 :
                        return False 
                    else :
                        wallet[5]-=1
                        wallet[10]-=1
                        wallet[20]+=1
        return True