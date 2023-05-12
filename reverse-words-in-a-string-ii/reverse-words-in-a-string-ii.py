class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def reverse(start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        s.reverse()
        i, j = 0, 0

        while j < len(s):
            if s[j] != " ":
                j += 1
                if j == len(s)-1:
                    reverse(i, j)
                                     
            else:
                reverse(i, j-1)
                i = j = j+1




        