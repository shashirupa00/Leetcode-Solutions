from collections import defaultdict
from typing import List

class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        # Create adjacency list representation of the graph
        hashMap = defaultdict(set)
        for u, v in edges:
            hashMap[u].add(v)
            hashMap[v].add(u)
        
        # Find nodes with odd degree
        odds = []
        for i in range(1, n + 1):
            if len(hashMap[i]) % 2 != 0:
                odds.append(i)
        
        # If the number of odd degree nodes is not 0, 2, or 4, return False
        if len(odds) % 2 != 0 or len(odds) > 4:
            return False
        
        # If there are 0 odd nodes, return True (no need to add any edges)
        if len(odds) == 0:
            return True
        
        # Helper function to check if we can add an edge without creating a duplicate edge
        def can_add_edge(u, v):
            return v not in hashMap[u]
        
        # If there are 2 odd nodes, check if they can be connected directly or through an intermediate node
        if len(odds) == 2:
            u, v = odds
            if can_add_edge(u, v):
                return True
            for i in range(1, n + 1):
                if i != u and i != v and can_add_edge(u, i) and can_add_edge(v, i):
                    return True
            return False
        
        # If there are 4 odd nodes, check all combinations to see if we can add two edges to make degrees even
        if len(odds) == 4:
            u, v, x, y = odds
            possible_pairs = [(u, v), (u, x), (u, y), (v, x), (v, y), (x, y)]
            for i in range(len(possible_pairs)):
                for j in range(i + 1, len(possible_pairs)):
                    (a, b), (c, d) = possible_pairs[i], possible_pairs[j]
                    if len({a, b, c, d}) == 4 and can_add_edge(a, b) and can_add_edge(c, d):
                        return True
            return False
        
        return False