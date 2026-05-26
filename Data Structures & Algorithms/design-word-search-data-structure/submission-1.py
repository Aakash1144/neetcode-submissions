from typing import List

class prefixNode:
    def __init__(self):
        self.childrens = {}
        self.is_end_of_word = False


class WordDictionary:
    def __init__(self):
        self.root = prefixNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if not node.childrens.get(c):
                node.childrens[c] = prefixNode()
            node = node.childrens[c]
        node.is_end_of_word = True

    def search_old(self, word: str) -> bool:
        node = self.root
        for c in word:
            if not node.childrens.get(c):
                return False
            node = node.childrens[c]
        return node.is_end_of_word

    def search(self, word: str) -> bool:
        node = self.root
        def dfs(index, node):
            if index == len(word):
                return node.is_end_of_word
            c = word[index]
            if c!= '.':
                if c not in node.childrens:
                    return False
                return dfs(index+1, node.childrens[c])
            
            for node in node.childrens.values():
                if(dfs(index+1, node)):
                    return True

            return False   
        return dfs(0,node)


    def autocomplete(self, prefix: str) -> List[str]:
        node = self.root
        for c in prefix:
            if c not in node.childrens:
                return []
            node = node.childrens[c]
            
        results = []

        def dfs(curr_node, curr_word):
            if curr_node.is_end_of_word:
                results.append(curr_word)
            for c, child_node in curr_node.childrens.items():
                dfs(child_node, curr_word + c)
                                                                                                                                                                                                                                                                                                    
        dfs(node, prefix)
        return results
