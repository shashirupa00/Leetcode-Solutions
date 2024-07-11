class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        hashMap = defaultdict(list)
        level = 0
        i = 0
        tempStr = ""

        while i < len(s):
            
            if s[i] in ["(", ")"]: 
                
                if s[i] == '(':
                    level += 1
                if s[i] == ')':
                    level -= 1

                i += 1
                continue 

            while i < len(s) and s[i].isalpha():

                tempStr += s[i]
                i += 1
            
            hashMap[level].append(tempStr)
            tempStr = ""

        level = max(hashMap)
        res = ""

        while level > 0:

            s1 = hashMap[level][0] if len(hashMap[level]) > 0 else ""
            s2 = hashMap[level][1] if len(hashMap[level]) == 2 else ""

            res = s1 + res + s2
            res = res[::-1]
            level -= 1
        
        if 0 in hashMap:
            s1 = hashMap[0][0] if len(hashMap[0]) > 0 else ""
            s2 = hashMap[0][1] if len(hashMap[0]) == 2 else ""
            res = hashMap[0][0] + res + (hashMap[0][1] if len(hashMap[0]) == 2 else "")
            
        return res