class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)-1
        stack = [(temperatures[n], n)]
        res = [0 for i in range(len(temperatures))]

        for i in range(len(temperatures)-2, -1, -1):
            
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()

            if len(stack) == 0:
                stack.append((temperatures[i], i))
                continue

            res[i] = stack[-1][1] - i
            stack.append((temperatures[i], i))
        
        return res


        
        