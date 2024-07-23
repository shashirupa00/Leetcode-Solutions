class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [(temperatures[-1], len(temperatures) - 1)]
        res = [0 for i in range(len(temperatures))]

        for i in range(len(temperatures) - 2, -1, -1):

            temp = temperatures[i]

            while stack and stack[-1][0] < temp:
                stack.pop()
            
            if stack:
                res[i] = stack[-1][1] - i

            stack.append((temp, i))
        
        return res