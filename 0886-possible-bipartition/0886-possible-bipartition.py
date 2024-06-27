class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        visited = set()
        res = True

        def bfs(start):
        
            deq = collections.deque([(start, 0)])
            hashMap = defaultdict(list)
            groupMap = {start: 0}

            for s, e in dislikes:
                hashMap[s].append(e)
            
            while deq:
                for i in range(len(deq)):

                    node, level = deq.popleft()
                    
                    for nxt in hashMap[node]:
                        if nxt in groupMap:
                            if groupMap[nxt] != (level + 1) % 2:   return False
                        else:
                            deq.append((nxt, level + 1)) 
                            groupMap[nxt] = (level + 1) % 2
                            visited.add(nxt)

            return True
        
        for i in range(n):
            if i not in visited:
                visited.add(i)
                if not bfs(i): return False
        
        return True