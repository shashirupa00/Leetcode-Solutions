class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        if s == "":
            return 0
        res = 0

        def helper(word):
         
            arr = []
            temp = ""
            for i, char in enumerate(word):
                if not temp or temp[-1] == char:
                    temp += char  # Add character to the current group
                else:
                    arr.append(temp)  # Append the group to the list
                    temp = char  # Start a new group
            arr.append(temp)  # Append the last group
            return arr
        
        stretchyArr = helper(s)

        for word in words:
            flag = True
            sWord = helper(word)
            
            if len(sWord) != len(stretchyArr):  # Group counts must match
                continue
            
            for i, char in enumerate(stretchyArr):
                if char == sWord[i]:
                    continue
                # If the first character matches and stretchyArr's group is 3 or more
                if char[0] == sWord[i][0] and len(char) >= 3:
                    extraLength = len(char) - len(sWord[i])
                    # Ensure the word's group can be stretched to match
                    if len(sWord[i]) + extraLength < 3:
                        flag = False
                        break
                else:
                    flag = False
                    break

            if flag:
                res += 1
        
        return res