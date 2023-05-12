class Solution:
    def isValid(self, s: str) -> bool:

        deq = collections.deque()
        hashMap = {'{':'}', '(':')', '[':']'}

        for bracket in s:
            if bracket in hashMap:
                deq.append(bracket)
            else:
                if deq and hashMap[deq[-1]] == bracket:
                    deq.pop()
                else:
                    return False

        return False if deq else True