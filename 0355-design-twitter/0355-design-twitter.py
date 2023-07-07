class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = collections.defaultdict(list)
        self.followMap = collections.defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((tweetId, self.time))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []
        
        if userId not in self.followMap[userId]:
            self.followMap[userId].add(userId)

        if userId in self.followMap:
            for followee in self.followMap[userId]:
                for tweet in self.tweetMap[followee]:
                    curTime, tId = tweet[1], tweet[0]
                    maxHeap.append((curTime, tId))

            heapq.heapify(maxHeap)

            while len(res) < 10 and maxHeap:
                curTime, tId = heapq.heappop(maxHeap)
                res.append(tId)

        return res      

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap:
            self.followMap[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)