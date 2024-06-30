class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        res = [set() for i in range(n)]
        deq = collections.deque([])
        graph = collections.defaultdict(list)
        degree = [0 for i in range(n)]

        for u, v in edges:
            graph[u].append(v)
            degree[v] += 1
        
        for node, d in enumerate(degree):
            if not d:
                deq.append(node)
        
        topOrder = []
        
        while deq:

            curNode = deq.popleft()
            topOrder.append(curNode)

            for nxt in graph[curNode]:
                degree[nxt] -= 1
                if not degree[nxt]:
                    deq.append(nxt)
        
        for node in topOrder:
            for nxt in graph[node]:
                res[nxt].add(node)
                res[nxt].update(res[node])
        
        for i in range(len(res)):
            res[i] = sorted(list(res[i]))

        return res        