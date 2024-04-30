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

        diff = 0
        root = self
        print(word)

        def dfs(i, cur):

            nonlocal diff

            if diff > 1:
                return False

            if i == len(word):
                return diff == 1 and cur.isEnd
            
            letter = word[i]
            
            if letter not in cur.children and diff == 0:
                diff = 1
                for nxt in cur.children:
                   return dfs(i+1, cur.children[nxt])
            
            else:
               return dfs(i+1, cur.children[letter])
        
        return dfs(0, root)

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