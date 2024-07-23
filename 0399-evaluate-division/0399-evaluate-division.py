class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        hashMap = defaultdict(list)
        res = []

        for i in range(len(values)):
            src, dst = equations[i]
            hashMap[src].append((dst, values[i]))
            hashMap[dst].append((src, 1 / values[i]))
        
        def bfs(node, target):
            
            deq = collections.deque([(node, 1)])
            ans = -1
            visited = set()

            if node not in hashMap or target not in hashMap:
                return -1

            while deq:
                cur, val = deq.popleft()

                if cur == target:
                    ans = val
                    break
                
                for nxt, nxtVal in hashMap[cur]:
                    if nxt not in visited:
                        deq.append((nxt, val * nxtVal))
                        visited.add(nxt)

            return ans
        
        for src, dst in queries:
            res.append(bfs(src, dst))
        
        return res