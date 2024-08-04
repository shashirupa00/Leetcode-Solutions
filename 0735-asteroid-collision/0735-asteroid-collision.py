class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for asteroid in asteroids:

            # Pops out all the asteroids that lose the collision battle with the current asteroid
            while stack and stack[-1] > 0 and asteroid < 0 and abs(asteroid) > stack[-1]:
                stack.pop()
            
            if stack and stack[-1] > 0 and asteroid < 0:
                if stack[-1] == abs(asteroid):
                    stack.pop()
                continue
            
            stack.append(asteroid)
        
        return stack


        