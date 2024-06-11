class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        res = []
        counter = Counter(arr1)
        temp = []
        newArr = set(arr2)

        for num in arr2:
            res.extend([num] * counter[num])
        
        for num in arr1:
            if num not in newArr:
                temp.append(num)
        
        res.extend(sorted(temp))
        
        return res
