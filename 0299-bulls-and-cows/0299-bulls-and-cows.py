class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        bulls, cows = 0, 0
        hashMap = defaultdict(int)
        arr = []

        for i, num in enumerate(guess):
            
            if guess[i] == secret[i]:
                bulls += 1
            
            else:
                arr.append(i)
                hashMap[num] += 1
        
        for i in range(len(arr)):

            x = secret[arr[i]]

            if secret[arr[i]] in hashMap:
                cows += 1
                hashMap[secret[arr[i]]] -= 1
                if not hashMap[secret[arr[i]]]: del hashMap[secret[arr[i]]]
    
        return str(bulls) + 'A' + str(cows) + 'B'