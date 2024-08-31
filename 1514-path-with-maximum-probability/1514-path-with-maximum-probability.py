class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        hashMap = defaultdict(list)
        res = 0

        for i in range(len(edges)):
            src, dst, prob = edges[i][0], edges[i][1], succProb[i]
            hashMap[src].append((dst, prob))
            hashMap[dst].append((src, prob))
        
        def dfs(node, visited, curProb):

            nonlocal res
            
            if node in visited:
                return
            
            visited.add(node)
            
            if node == end_node:
                res = max(res, curProb)

            for nxt, prob in hashMap[node]:
                if nxt not in visited:
                    dfs(nxt, visited, curProb * prob)
            
            visited.remove(node)

        dfs(start_node, set(), 1)
        return res