class Solution:
    def minSwaps(self, s: str) -> int:
        
        size = 0

        for char in s:

            if size and char == ']':
                size -= 1
            
            elif char == '[':
                size += 1
        
        return (size + 1) // 2