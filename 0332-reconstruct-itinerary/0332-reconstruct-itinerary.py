class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        res = ["JFK"]
        hashMap = collections.defaultdict(collections.deque)

        tickets.sort()

        for fro, to in tickets:
            hashMap[fro].append(to)
        
        def dfs(vertex):

            nonlocal res

            if len(res) == len(tickets)+1:
                return True
            if vertex not in hashMap:
                return False
            
            temp = list(hashMap[vertex])

            for i in range(len(temp)):
                curr = hashMap[vertex].popleft()
                res.append(curr)

                if dfs(curr): return True

                res.pop()
                hashMap[vertex].append(curr)
                       
            return False
        
        dfs("JFK")
        return res        