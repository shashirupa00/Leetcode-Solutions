class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
    
        res = 0

        for i in range(len(word)):

            vowelSet = set()
            consonantCount = 0

            for j in range(i, len(word)):

                if word[j] in set(['a', 'e', 'i', 'o', 'u']):
                    vowelSet.add(word[j])

                else:
                    consonantCount += 1
                    if consonantCount > k:
                        break

                if len(vowelSet) == 5 and consonantCount == k:
                        res += 1
                        
        return res