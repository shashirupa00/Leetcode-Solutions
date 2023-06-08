class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        hashMap = {}
        size, end = 0, 0
        res = []

        for i in range(len(s)):
            hashMap[s[i]] = i
        
        for i in range(len(s)):

            end = max(end, hashMap[s[i]])
            size += 1

            if i == end:
                res.append(size)
                size = 0
        
        return res

        

    