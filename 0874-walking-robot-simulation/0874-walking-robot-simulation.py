class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        obstacles = set([tuple(o) for o in obstacles])
        curDirection = (0, 1) # -1: N -> E, E -> S, S -> W, W -> N ; -2: N -> W, W -> S, S -> E, E -> N
        leftDirection = {(0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0), (1, 0): (0, 1)}
        rightDirection = {(0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1)}
        res = 0
        curPos = [0, 0]

        print(obstacles)

        for num in commands:

            if num == -1:
                curDirection = rightDirection[curDirection]
                continue
            
            if num == -2:
                curDirection = leftDirection[curDirection]
                continue

            x, y = curDirection
            tempX, tempY = curPos[0], curPos[1]

            for i in range(num):

                if x:
                    if (tempX + x, tempY) in obstacles:
                        break
                    tempX += x
                
                if y:
                    if (tempX, tempY + y) in obstacles:
                        break
                    tempY += y

            curPos = [tempX, tempY]

            res = max(res, curPos[0]**2 + curPos[1]**2)
        
        return res