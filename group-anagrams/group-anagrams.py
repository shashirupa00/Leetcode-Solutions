class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        def findKey(word):
            key = []
            for char in word:
                key.append(char)
            
            return tuple(sorted(key))
        
        hashMap = defaultdict(list)
        
        for word in strs:
            key = findKey(word)
            hashMap[key].append(word)
            
        return list(hashMap.values())
            
        