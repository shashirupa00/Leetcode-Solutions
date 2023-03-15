class Solution:
    def minJumps(self, arr: List[int]) -> int:

        if len(arr) == 1:
            return 0

        if arr[0] == arr[len(arr)-1]:
            return 1

        hashMap = collections.defaultdict(list)
        visited = set()
        q = collections.deque([0])
        steps = 0

        for i in range(len(arr)):
            hashMap[arr[i]].append(i)

        while q:
            
            for _ in range(len(q)):
                curr = q.pop()
                visited.add(curr)
                
                if curr == len(arr)-1:
                    return steps

                if curr-1 in range(0,len(arr)) and curr-1 not in visited: 
                    q.appendleft(curr-1)
                    visited.add(curr-1)

                if curr+1 in range(0,len(arr)) and curr+1 not in visited:
                    q.appendleft(curr+1)
                    visited.add(curr+1)

                for val in hashMap[arr[curr]]:
                    if val not in visited:
                        q.appendleft(val)
                del(hashMap[arr[curr]])

            steps += 1















        