class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        
        hamSet = [i for i in range(len(hamsters)) if hamsters[i] == "H"]
        res = set()

        for i in hamSet:
            
            if i-1 in res or i+1 in res:
                continue
            
            if i + 1 < len(hamsters) and hamsters[i+1] == ".":
                res.add(i+1)
            
            elif i - 1 >= 0 and hamsters[i-1] == ".":
                res.add(i-1)
            
            else:
                return -1
        
        return len(res)