class Solution:
    def confusingNumber(self, n: int) -> bool:
        
        hashMap = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        n = str(n)
        newNum = ""

        if len(n) == 1 and n in ("6", "9"):
            return True

        for char in n:
            if char not in hashMap:
                return False
            newNum += hashMap[char]
        
        return newNum != newNum[::-1]