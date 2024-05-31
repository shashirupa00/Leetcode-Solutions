class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        
        res = []
        i, j = 0, 0
        n, m = len(encoded1), len(encoded2)

        while i < n or j < m:

            n1, f1 = encoded1[i][0], encoded1[i][1]
            n2, f2 = encoded2[j][0], encoded2[j][1]
            newPair = []

            if f1 > f2:
                newPair = [n1 * n2, f2]
                encoded1[i][1] = f1 - f2
                j += 1
            
            elif f2 > f1:
                newPair = [n1 * n2, f1]
                encoded2[j][1] = f2 - f1
                i += 1
            
            else:
                newPair = [n1 * n2, f1]
                i += 1
                j += 1
            
            if res and res[-1][0] == newPair[0]: res[-1][1] += newPair[1]
            else: res.append(newPair)
        
        return res      