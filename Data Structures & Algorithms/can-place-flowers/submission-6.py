class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
##false [1,0,1,0,0,1,0] n=1
        if len(flowerbed)==1 :
            if n :
                if flowerbed==[0] :
                    return True
                else :
                    return False
            
        for i in range(len(flowerbed)):
            if flowerbed[i]==0 :
                if i==0 and i+1<len(flowerbed) and flowerbed[i+1]==0 :
                    flowerbed[i]=1
                    n-=1
                if i and i+1<len(flowerbed) and flowerbed[i-1]==0 and flowerbed[i+1]==0 :
                    flowerbed[i]=1
                    n-=1
                if i==len(flowerbed)-1 and i-1>=0 and flowerbed[i-1]==0 :
                    flowerbed[i]=1
                    n-=1

        return n<=0