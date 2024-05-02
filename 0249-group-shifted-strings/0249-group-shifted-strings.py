class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        hashMap = collections.defaultdict(list)

        for s in strings:
            key = ""
            shift = ord(s[0]) -  ord("a")
            for char in s:
                cur = ord(char) - shift
                key += chr(123 - (97 - cur)) if ord(char) - shift < 97 else chr(ord(char) - shift)
            hashMap[key].append(s)
        
        return list(hashMap.values())