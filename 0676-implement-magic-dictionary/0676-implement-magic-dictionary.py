class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False

    def add(self, word):

        cur = self

        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = Trie()
            cur = cur.children[letter]

        cur.isEnd = True

    def search(self, word):  

        def dfs(node, index, diff):
            if index == len(word):
                return diff == 1 and node.isEnd
            if diff > 1:
                return False

            found = False
            for char in node.children:
                if char == word[index]:
                    found |= dfs(node.children[char], index + 1, diff)
                else:
                    found |= dfs(node.children[char], index + 1, diff + 1)
            return found

        return dfs(self, 0, 0)

class MagicDictionary:

    def __init__(self):

        self.root = Trie()

    def buildDict(self, dictionary: List[str]) -> None:

        for word in dictionary:
            self.root.add(word)
        
    def search(self, searchWord: str) -> bool:

        return self.root.search(searchWord)
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)