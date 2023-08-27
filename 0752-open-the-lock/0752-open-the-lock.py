class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        if "0000" in deadends:
            return -1

        def findComb(lock):
            res = []

            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i + 1 :])
                digit = str((int(lock[i]) + 10 - 1) % 10)
                res.append(lock[:i] + digit + lock[i + 1 :])

            return res


        deq = collections.deque(["0000"])
        visited = set(deadends)
        moves = 0

        while deq:
            for _  in range(len(deq)):

                cur = deq.popleft()

                if cur == target:
                    return moves

                for comb in findComb(cur):
                    if comb not in visited:
                        visited.add(comb)
                        deq.append(comb)

            moves += 1
        
        return -1