class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stack = []
        res = 0

        for char in s:

            if char == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    res += 1
            
            else:
                stack.append(char)
        
        return len(stack) + res