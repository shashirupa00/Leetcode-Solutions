class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        deq = collections.deque([])
        visited = set()
        maxLen = 0

        for i in range(len(s)):

            if s[i] in visited:
                
                maxLen = max(maxLen, len(visited))

                while True:
                    temp = deq.popleft()
                    visited.remove(temp)
                    if temp == s[i]:
                        break


            deq.append(s[i])
            visited.add(s[i])
        
        return max(maxLen, len(deq))

            






        
        