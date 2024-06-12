class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:

        ages.sort()
        res = 0

        for i in range(len(ages)):

            if ages[i] <= 14:
                continue

            upperLimit = ages[i]
            lowerLimit = min(ages[i], int((0.5 * ages[i]) + 8))

            lo = bisect.bisect_left(ages, lowerLimit)
            hi = bisect.bisect_right(ages, upperLimit)

            res += hi - 1 - lo

        return res