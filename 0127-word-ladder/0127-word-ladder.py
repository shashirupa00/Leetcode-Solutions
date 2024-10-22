class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        hashMap = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '*' + word[i+1:]
                hashMap[key].append(word)
        
        deq = collections.deque([beginWord])
        visited = set()
        res = 0

        while deq:
            for _ in range(len(deq)):

                cur = deq.popleft()
                visited.add(cur)

                if cur == endWord:
                    return res + 1
                
                for i in range(len(cur)):
                    key = cur[:i] + '*' + cur[i+1:]
                    for nei in hashMap[key]:
                        if nei not in visited:
                            deq.append(nei)
            res += 1
        
        return 0