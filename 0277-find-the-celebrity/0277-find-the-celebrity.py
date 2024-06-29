# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        
        celeb = 0

        for i in range(1, n):

            if knows(celeb, i) and not knows(i, celeb):
                celeb = i
        
        flag = True

        print(celeb)

        for i in range(n):
            
            if i != celeb:
                print(i, celeb, knows(i, celeb))

                if (not knows(i, celeb) or knows(celeb, i)):
                    flag = False
        
        return celeb if flag else -1
        
        