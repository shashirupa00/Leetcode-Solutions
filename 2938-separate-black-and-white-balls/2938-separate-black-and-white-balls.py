class Solution:
    def minimumSteps(self, s: str) -> int:
        
        i = 0
        while i < len(s) and s[i] == '0':
            i += 1
    
        s = [char for char in s[i:]]
        curPos, curZero = 0, s.index('0') if '0' in s else None
        res = 0
        zeroCount = sum([1 for num in s if num == '0'])

        if not curZero: return 0

        while curPos < zeroCount:

            if s[curPos] == '1':

                res += curZero - curPos
                s[curPos], s[curZero] = "0", "1" 
                
                while curZero < len(s) and s[curZero] == '1':
                    curZero += 1

            curPos += 1
        
        return res