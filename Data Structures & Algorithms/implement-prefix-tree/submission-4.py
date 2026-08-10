class Trie:
    def __init__(self, word_exists_here: bool = False):
        self.next = [None for i in range(26)]
        self.word_exists_here = word_exists_here
    
    @staticmethod
    def to_trie_index(char):
        return ord(char) - ord("a")


class PrefixTree:
    def __init__(self):
        self.trie = Trie(word_exists_here=False)

    def insert(self, word: str) -> None:
        traverser = self.trie

        for char_idx, char in enumerate(word):
            idx = Trie.to_trie_index(char)

            if not traverser.next[idx]:
                traverser.next[idx] = Trie()

            traverser = traverser.next[idx]
            
        traverser.word_exists_here = True

    def search(self, word: str) -> bool:
        traverser = self.trie

        for char in word:
            idx = Trie.to_trie_index(char)

            if not traverser.next[idx]:
                return False
            
            traverser = traverser.next[idx]
        
        return traverser.word_exists_here

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return any(traverser.next)

        traverser = self.trie

        for char in prefix:
            idx = Trie.to_trie_index(char)

            if not traverser.next[idx]:
                return False
            
            traverser = traverser.next[idx]
        
        return True
        