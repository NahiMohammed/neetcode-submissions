class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i=0
        k=0
        while i <len(flowerbed) :
            if flowerbed[i]==1:
                i+=1

            else :
                if i+2<len(flowerbed) and flowerbed[i+1]==0 and flowerbed[i+2]==0 :
                    k+=1
                i=min(i+2,len(flowerbed)-1)
        if k>=n :
            return True
        return False
                
        