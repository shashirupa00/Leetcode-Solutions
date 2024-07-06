class Solution:
    def passThePillow(self, n: int, time: int) -> int:

        direction = 1
        
        while time > (n - 1):
            time = time - (n - 1)
            direction *= -1
        
        if direction == 1:
            return 1 + time
        
        else:
            return n - time