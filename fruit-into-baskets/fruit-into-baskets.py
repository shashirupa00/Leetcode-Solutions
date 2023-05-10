class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        mtf = 1
        l, r = 0, 1
        hashMap = {fruits[l]: 0}

        while r < len(fruits):
            
            if fruits[r] in hashMap:
                hashMap[fruits[r]] = r

            if fruits[r] not in hashMap and len(hashMap) < 2:
                hashMap[fruits[r]] = r

            if len(hashMap) >= 2 and fruits[r] not in hashMap:
                l = min(hashMap.values())
                temp = fruits[l]
                l = hashMap[fruits[l]] + 1
                hashMap.pop(temp)
                hashMap[fruits[r]] = r
            
            mtf = max(mtf, r-l+1)
            r += 1

        return mtf
