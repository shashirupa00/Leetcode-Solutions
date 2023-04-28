class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashMap, res = {}, []

        def findKey(word):
            l = []
            for letter in word:
                l.append(letter)

            return tuple(sorted(l))

        for word in strs:
            key = findKey(word)
            if key not in hashMap:
                hashMap[key] = []
            hashMap[key].append(word)

        for values in hashMap.values():
            res.append(values)
        
        return res

        




        
            
        