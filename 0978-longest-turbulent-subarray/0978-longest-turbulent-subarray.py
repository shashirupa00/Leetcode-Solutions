class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 1
        temp = 1

        for i in range(len(arr)-1):
            if i % 2 == 0 and arr[i] > arr[i+1]:
                temp += 1
                res = max(res, temp)
            elif i % 2 == 1 and arr[i] < arr[i+1]:
                temp += 1
                res = max(res, temp)
            else:
                temp = 1
        
        temp = 1

        for i in range(len(arr)-1):
            if i % 2 == 0 and arr[i] < arr[i+1]:
                temp += 1
                res = max(res, temp)
            elif i % 2 == 1 and arr[i] > arr[i+1]:
                temp += 1
                res = max(res, temp)
            else:
                temp = 1
        
        return res
