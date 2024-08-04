class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        stack = [-1]
        res = 0

        for i, char in enumerate(s):

            if char == '(':
                stack.append(i)
            
            else:
                stack.pop()

                if stack: res = max(res, i - stack[-1])

                if not stack: stack.append(i)
        
        return res