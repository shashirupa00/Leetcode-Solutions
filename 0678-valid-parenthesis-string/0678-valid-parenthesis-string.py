class Solution:
    def checkValidString(self, s: str) -> bool:

        leftMax, leftMin = 0, 0

        for char in s:

            if char == "(":
                leftMax, leftMin = leftMax+1, leftMin+1
            elif char == ")":
                leftMax, leftMin = leftMax-1, leftMin-1
            else:
                leftMax, leftMin = leftMax+1, leftMin-1            
            if leftMax<0: 
                return False
            if leftMin<0: 
                leftMin = 0
        
        return leftMin==0
        