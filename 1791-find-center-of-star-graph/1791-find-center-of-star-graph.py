class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        hashMap = defaultdict(list)

        for u, v in edges:
            hashMap[u].append(v)
            hashMap[v].append(u)
        
        for node in hashMap:
            if len(hashMap[node]) == len(edges):
                return node