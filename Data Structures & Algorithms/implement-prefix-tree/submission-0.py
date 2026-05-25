class prefixNode:
    def __init__(self):
        self.childrens = {}
        self.is_end_of_word = False
class PrefixTree:

    def __init__(self):
        self.root = prefixNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if not node.childrens.get(c):
                node.childrens[c] = prefixNode()
            node = node.childrens[c]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if not node.childrens.get(c):
                return False
            node = node.childrens[c]
        return node.is_end_of_word
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if not node.childrens.get(c):
                return False
            node = node.childrens[c]
        return True
        