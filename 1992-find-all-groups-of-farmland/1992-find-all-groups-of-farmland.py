class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:

        visited = set()
        rows, cols = len(land), len(land[0])
        res = []
        tempRes = [-1, -1]

        def check(i, j):

            a, b = i + 1, j
            c, d = i, j + 1
            aInBounds = a in range(rows)
            dInBounds = d in range(cols)

            if (a == rows or aInBounds) and (d == cols or dInBounds):
                if (a == rows or land[a][b] == 0) and (d == cols or land[c][d] == 0):
                    return True


        def dfs(i, j):

            nonlocal tempRes

            if i not in range(rows) or j not in range(cols) or (i, j) in visited or land[i][j] == 0:
                return

            visited.add((i, j))

            if check(i, j):
                tempRes = [i, j]

            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)

            return

        for i in range(rows):
            for j in range(cols):
                if land[i][j] == 1 and (i, j) not in visited:
                    temp = [i, j]
                    dfs(i, j)
                    if tempRes != [-1, -1]:
                        temp.extend(tempRes)
                        tempRes = [-1, -1]
                    res.append(temp)

        return res