class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.wordPresent = ""

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):

        cur = self.root

        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]
        
        cur.isEnd = True
        cur.wordPresent = word
    
    def search(self, word):

        cur = self.root

        for letter in word:
            if letter not in cur.children:
                return ""

            cur = cur.children[letter]

            if cur.isEnd:
                return cur.wordPresent
        
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        root = Trie()
        words = sentence.split(" ")

        for word in dictionary:
            root.insert(word)
        
        for i, word in enumerate(words):
            temp = root.search(word)
            if temp:
                words[i] = temp
        
        return " ".join(words)