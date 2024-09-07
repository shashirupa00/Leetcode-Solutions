class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        for char in s:

            if char == '[':
                stack.append(char)
                continue

            elif char == ']':

                curString = stack.pop()
                stack.pop()
                curNum = stack.pop()

                newStr = int(curNum) * curString

                if stack and stack[-1].isalpha():
                    stack[-1] += newStr

                else:
                    stack.append(newStr)
            
            else:
                if char.isalpha():
                    if stack and stack[-1].isalpha():
                        stack[-1] += char
                    else:
                        stack.append(char)
                else:
                    if stack and stack[-1].isdigit():
                        stack[-1] += char
                    else:
                        stack.append(char)
        
        return "".join(stack)