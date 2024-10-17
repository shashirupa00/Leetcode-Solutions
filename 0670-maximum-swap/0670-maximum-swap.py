class Solution:
    def maximumSwap(self, num: int) -> int:
        
        arr = []
        newNum = [char for char in str(num)]

        for i, char in enumerate(str(num)):
            arr.append((char, i))

        for i in range(len(arr) - 2, -1, -1):
            if arr[i][0] <= arr[i + 1][0]:
                arr[i] = arr[i + 1]
        
        for i in range(len(arr)):

            if newNum[i] < arr[i][0]:

                swap1, swap2 = i, arr[i][1]
                newNum[swap1], newNum[swap2] = newNum[swap2], newNum[swap1]
                break
        
        return int("".join(newNum))