class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        
        for i, time in enumerate(times):
            time.append(i)
        
        times.sort()
        chairs = [i for i in range(len(times))]
        hashMap = {}
        leaves = []

        for start, leave, friend in times:

            while leaves and leaves[0][0] <= start:
                _, chair = heapq.heappop(leaves)
                heapq.heappush(chairs, chair)
            
            chair = heapq.heappop(chairs)
            hashMap[friend] = chair

            heapq.heappush(leaves, (leave, chair))

            if friend == targetFriend:
                return chair

        return -1 