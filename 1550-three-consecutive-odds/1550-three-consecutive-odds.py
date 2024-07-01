class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        
        flag = 0

        for num in arr:
            if num % 2:
                flag += 1
                if flag == 3: return True
            else:
                flag = 0
        
        return False