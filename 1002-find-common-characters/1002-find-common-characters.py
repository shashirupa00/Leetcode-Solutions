class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        arr = []
        setList = []
        res = []

        for word in words:
            arr.append(Counter(word))
            temp = set()
            for letter in word:
                temp.add(letter)
            setList.append(temp)
        
        common = set.intersection(*setList)
        
        for letter in common:
            temp = [letter, float("inf")]
            for word in arr:
                temp[1] = min(temp[1], word[letter])
            x = [letter] * temp[1]
            res.extend(x)

        return res
            

        
