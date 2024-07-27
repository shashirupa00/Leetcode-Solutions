class Solution:
    def minimumCost(self, sourceString: str, targetString: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        hashMap = defaultdict(list)
        res = 0
        minCost = {}

        for src, dst, cst in zip(original, changed, cost):
            hashMap[src].append((cst, dst))

        def shortestPath(source, dest) -> int:
            
            paths = {}
            minHeap = hashMap[source][:]
            heapq.heapify(minHeap)

            while minHeap:

                curCost, curNode = heapq.heappop(minHeap)

                if curNode == dest:
                    return curCost
                
                paths[curNode] = curCost

                for nxtCost, nxt in hashMap[curNode]:
                    if nxt not in paths:
                        heapq.heappush(minHeap, (curCost + nxtCost, nxt))
            
            return -1

        for i in range(len(sourceString)):
            source, dest = sourceString[i], targetString[i]
            if source != dest:
                if (source, dest) in minCost:
                    res += minCost[(source, dest)]
                else:
                    temp = shortestPath(source, dest)
                    if temp != -1:
                        res += temp
                    else:
                        return -1
                    minCost[(source, dest)] = temp

        return res