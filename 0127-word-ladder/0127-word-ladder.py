class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        hashMap = collections.defaultdict(list)
        wordList.append(beginWord)
        deq = collections.deque([beginWord])
        visited = set([beginWord])
        res = 1

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                hashMap[pattern].append(word)
        
        while deq:
            for _ in range(len(deq)):
                word = deq.popleft()
                if word == endWord:
                    return res
                
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i+1:]
                    for w in hashMap[pattern]:
                        if w not in visited:
                            visited.add(w)
                            deq.append(w)

            res += 1

        return 0
        