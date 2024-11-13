class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:

        items.sort()
        itemMap = {}
        res = []

        for price, beauty in items:
            itemMap[price] = max(itemMap.get(price, 0), beauty)
        
        arr = [key for key in itemMap]

        for i in range(1, len(arr)):
            itemMap[arr[i]] = max(itemMap[arr[i]], itemMap[arr[i - 1]])

        for q in queries:

            if q < arr[0]:
                res.append(0)
                continue

            idx = bisect.bisect_right(arr, q)
            res.append(itemMap[arr[idx - 1]])
        
        return res
            