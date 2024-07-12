class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        def helper(score, match):
            stack = []
            res = 0

            for char in s:

                if stack and char == match[-1] and stack[-1] == match[0]:
                    stack.pop()
                    res += score
                
                else:
                    stack.append(char)
        
            return ('').join(stack), res
        
        if x > y:
            s, score1 = helper(x, "ab")
            s, score2 = helper(y, "ba")
            return score1 + score2
        
        s, score1 = helper(y, "ba")
        s, score2 = helper(x, "ab")

        return score1 + score2
