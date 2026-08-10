class TrieNode:
    def __init__(self, is_terminating: bool = False):
        self.next = {}
        self.is_terminating = is_terminating


class PrefixTree:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        traverser = self.trie

        for char in word:
            traverser.next[char] = traverser.next.get(char, TrieNode())
            traverser = traverser.next[char]
        
        traverser.is_terminating = True

    def search(self, word: str) -> bool:
        traverser = self.trie

        for char in word:
            if char not in traverser.next:
                return False

            traverser = traverser.next[char]

        return traverser.is_terminating

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            # if empty prefix, True if the user added an empty string
            # otherwise False
            return self.trie.is_terminating
        
        traverser = self.trie
        for char in prefix:
            if char not in traverser.next:
                return False

            traverser = traverser.next[char]
        
        return True
        
        