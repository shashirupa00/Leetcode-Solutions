class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = defaultdict(list)

        for src, dst in tickets:
            graph[src].append(dst)

        for src in graph:
            graph[src].sort(reverse=True) 
        
        itinerary = []
        
        def dfs(airport):
            while graph.get(airport, []):
                dfs(graph[airport].pop())
            itinerary.append(airport)
        
        dfs("JFK")
        return itinerary[::-1]    