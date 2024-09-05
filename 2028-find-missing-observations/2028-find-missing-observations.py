class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        
        mSum = sum(rolls)
        nSum = ((len(rolls) + n) * mean) - mSum
        roll = nSum / n
        
        if roll > 6 or roll < 1:
            return []
        
        res = [math.floor(roll)] * (n-1)

        remainingRoll = nSum - (math.floor(roll) * (n-1))

        i = 0
        while remainingRoll > 6 and i < len(res):
            temp = res[i]
            res[i] += (6 - temp)
            remainingRoll -= (6 - temp)
            i += 1
        
        if remainingRoll > 6:
            return []
            
        res.append(remainingRoll)
        
        return res