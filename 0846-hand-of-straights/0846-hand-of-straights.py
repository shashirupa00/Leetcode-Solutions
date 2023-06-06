class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0: return False

        hand.sort()
        hashMap = {}
        size = 0
        globalCount = 0

        for num in hand:
            hashMap[num] =  1 + hashMap.get(num, 0)
        
        while globalCount < len(hand):
            count = 0
            prev = -1
            for key in hashMap:
                if not hashMap[key]: continue

                if prev != -1 and key-prev != 1: return False

                hashMap[key] -= 1
                globalCount += 1
                prev = key

                count += 1
                if count == groupSize: 
                    size += 1
                    break
        
        return len(hand)//groupSize == size
