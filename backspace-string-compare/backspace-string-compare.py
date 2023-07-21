class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        deq = collections.deque([])

        for letter in s:

            if deq and letter == "#":
                deq.pop() 
            
            elif letter.isalpha():
                deq.append(letter)
        
        res1 = "".join(deq)

        deq = collections.deque([])
        for letter in t:

            if deq and letter == "#":
                deq.pop()
            
            elif letter.isalpha():
                deq.append(letter)
        
        res2 = "".join(deq)

        return res1 == res2
        