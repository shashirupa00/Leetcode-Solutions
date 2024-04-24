class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        hashMap = defaultdict(list)
        pattern = defaultdict(set)

        for u, t, w in sorted(zip(username, timestamp, website), key=lambda x: (x[0], x[1])):
            hashMap[u].append(w)

        for user, websites in hashMap.items():
            if len(websites) >= 3:
                seen_patterns = set(combinations(websites, 3))
                for p in seen_patterns:
                    pattern[p].add(user)

        patternScore = {p: len(u) for p, u in pattern.items()}
        maxScore = max(patternScore.values(), default=0)

        result = min((p for p in patternScore if patternScore[p] == maxScore), default=(), key=lambda x: x)

        return list(result)