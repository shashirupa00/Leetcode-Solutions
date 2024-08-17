class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        hashMap = collections.defaultdict(list)
        emailToNames = {}
        visited = set()
        components = []

        for account in accounts:
            for i in range(1, len(account)):
                emailToNames[account[i]] = account[0]
                for j in range(i+1, len(account)):
                   hashMap[account[i]].append(account[j])
                   hashMap[account[j]].append(account[i])
                if account[i] not in hashMap: hashMap[account[i]] = []
        
        def dfs(node):

            if not len(hashMap[node]) or node in visited:
                components[-1].add(node)
                return
            
            visited.add(node)
            components[-1].add(node)

            for nxt in hashMap[node]:
                dfs(nxt)
        

        for node in hashMap:
            if node not in visited:
                components.append(set())
                dfs(node)
                

        res = []

        for component in components:
            temp = []
            cur = list(component)
            temp.append(emailToNames[cur[0]])
            temp.extend(sorted(cur))
            res.append(temp)

        return res

            
