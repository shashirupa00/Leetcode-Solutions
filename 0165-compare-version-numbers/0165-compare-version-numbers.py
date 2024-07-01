class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        v1 = version1.split('.')
        v2 = version2.split('.')

        n, m = len(v1), len(v2)
        i, j = 0, 0

        while i < n or j < m:

            val1 = 0 if i >= n else int(v1[i])
            val2 = 0 if j >= m else int(v2[j])

            if val1 > val2: return 1

            elif val2 > val1: return -1

            i += 1
            j += 1
        
        return 0
        