class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        
        stack = []
        robots = [(positions[i], healths[i], directions[i], i) for i in range(len(positions))]

        robots.sort()

        def collision(d1, d2):
            return d1 == 'R' and d2 == 'L'

        for p, h, d, i in robots:

            newP, newH, newD, newI = p, h, d, i

            while stack and collision(stack[-1][-2], newD):

                prevP, prevH, prevD, prevI = stack.pop()

                if newH > prevH:
                    newH -= 1
                    newP = p
                    newD = d
                    newI = i
                
                elif newH < prevH:
                    newH = prevH - 1
                    newP = prevP
                    newD = prevD
                    newI = prevI
                
                else:
                    newP = None
                    break
            
            if newP:
                stack.append((newP, newH, newD, newI))

        newRobots = sorted(stack, key=lambda x:x[-1])
        
        return [h for p, h, d, i in newRobots]