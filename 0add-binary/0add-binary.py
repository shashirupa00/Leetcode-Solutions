class Solution:
    def addBinary(self, a, b) -> str:

        num1 = int(a, 2)
        num2 = int(b, 2)
        
        res = num1 + num2

        binary_str = format(int(res), 'b')
        return str(binary_str)
        
        
        