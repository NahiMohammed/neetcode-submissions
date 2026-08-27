class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        s = sum(flowerbed)
        if len(flowerbed)%2==0 :
            m=len(flowerbed)//2
        else :
            if len(flowerbed)>1 and flowerbed[1]==1 :
                m=len(flowerbed)//2
            else :
                m=len(flowerbed)//2 +1
        return m>=s+n

