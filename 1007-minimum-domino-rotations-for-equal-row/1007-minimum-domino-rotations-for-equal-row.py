class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        if not tops or not bottoms:
		
            return -1

        def helper(arr, num, arr2):
            rotationCounter = 0
            for i in range(len(arr)):
                if arr[i] == num:
                    continue
                if arr[i] != num and arr2[i] == num:
                    rotationCounter += 1
                else:
                    return float("inf")
            return rotationCounter

        res = float("inf")
        topCounter, bottomCounter = collections.Counter(tops), collections.Counter(bottoms)

        for num in topCounter:
            if topCounter[num] + bottomCounter[num] >= len(tops):
                res = min(helper(tops, num, bottoms), helper(bottoms, num, tops))

        return res if res != float("inf") else -1
