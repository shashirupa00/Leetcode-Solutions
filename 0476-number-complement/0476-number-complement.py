class Solution:
    def findComplement(self, num: int) -> int:
        
        newNum = [char for char in (str(bin(num))[2:])]
        newNum = [not int(char) for char in newNum]
        newNum = newNum[::-1]
        res = 0

        for i in range(len(newNum)):
            if newNum[i]: res += (2**i)
        
        return res