class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        obstacles = set([tuple(o) for o in obstacles])
        curDirection = (0, 1)
        leftDirection = {(0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0), (1, 0): (0, 1)}
        rightDirection = {(0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1)}
        res = 0
        curPos = [0, 0]

        for num in commands:

            if num == -1 or num == -2:
                curDirection = rightDirection[curDirection] if num == -1 else leftDirection[curDirection]
                continue

            x, y = curDirection
            tempX, tempY = curPos[0], curPos[1]

            for _ in range(num):

                if x and (tempX + x, tempY) not in obstacles:
                    tempX += x
                
                if y and (tempX, tempY + y) not in obstacles:
                    tempY += y

            curPos = [tempX, tempY]

            res = max(res, curPos[0]**2 + curPos[1]**2)
        
        return res