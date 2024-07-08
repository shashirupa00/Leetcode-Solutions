class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        lost = set()
        curPos = 1

        while len(lost) < n - 1:

            count = k

            while count:
                
                if curPos not in lost:
                    count -= 1

                if not count:
                    lost.add(curPos)

                curPos = (curPos + 1) % n
        
        for i in range(1, n+1):
            if i not in lost:
                return i
        