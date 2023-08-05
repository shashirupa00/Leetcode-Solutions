class SeatManager:

    def __init__(self, n: int):
        self.minHeap = [i for i in range(n)]
        heapq.heapify(self.minHeap)

    def reserve(self) -> int:
        seatNumber = heapq.heappop(self.minHeap)
        return seatNumber+1

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.minHeap, seatNumber-1)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)