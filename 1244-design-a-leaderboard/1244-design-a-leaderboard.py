class Leaderboard:

    def __init__(self):
        self.leaderBoard = {}

    def addScore(self, playerId: int, score: int) -> None:
        self.leaderBoard[playerId] = score + self.leaderBoard.get(playerId, 0)        

    def top(self, K: int) -> int:
        return (sum(sorted(list(self.leaderBoard.values()))[-K:]))
        
    def reset(self, playerId: int) -> None:
        self.leaderBoard[playerId] = 0
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)