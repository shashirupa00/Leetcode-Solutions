class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:

        curr = self.root

        for l in word:
            if l not in curr.children:
                curr.children[l] = TrieNode()
            curr = curr.children[l]
        
        curr.isWord = True

    def search(self, word: str) -> bool:

        curr = self.root
        
        for l in word:
            if l not in curr.children:
                return False
            curr = curr.children[l]

        if curr.isWord == True:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:

        curr = self.root 

        for l in prefix:
            if l not in curr.children:
                return False
            curr = curr.children[l]

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)