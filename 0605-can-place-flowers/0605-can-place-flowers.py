class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if len(flowerbed) == 1 and flowerbed[0] == 0:
            n -= 1
            return n <=0 
                
        for i in range(len(flowerbed)):
            
            if n == 0:  break

            if (flowerbed[i] == 0) and ((i == 0 and flowerbed[i+1] == 0) or
                (i == len(flowerbed)-1 and flowerbed[i-1] == 0) or
                ((0<i<len(flowerbed)-1) and flowerbed[i-1] == 0 and flowerbed[i+1] == 0)):

                flowerbed[i] = 1
                n -= 1

        return n == 0



