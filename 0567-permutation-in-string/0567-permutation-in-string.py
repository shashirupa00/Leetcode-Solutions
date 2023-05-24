class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        hashMap1, hashMap = {}, {}
        l, r = 0, len(s1)-1

        for char in s1:
            hashMap1[char] = 1 + hashMap1.get(char,0)
        
        for char in s2[:r]:
            hashMap[char] = 1 + hashMap.get(char,0)
        
        while r < len(s2):

            hashMap[s2[r]] = 1 + hashMap.get(s2[r], 0)

            if hashMap == hashMap1:
                return True
            
            hashMap[s2[l]] -= 1
            if hashMap[s2[l]] == 0:
                hashMap.pop(s2[l])
            l += 1
            r += 1
        
        return False
            
            




            






        
        

        