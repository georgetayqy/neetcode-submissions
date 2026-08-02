class PrefixTree:
    def __init__(self, has_prefix: bool = True, is_terminating: bool = False):
        self.neighbours = {}
        self.has_prefix = has_prefix
        self.is_terminating = is_terminating

    def insert(self, word: str) -> None:
        traverse = self

        for char in word:
            if char not in traverse.neighbours:
                pt = PrefixTree(has_prefix=True)
                traverse.neighbours[char] = pt
                traverse = pt
            else:
                traverse = traverse.neighbours[char]
        
        traverse.is_terminating = True

    def search(self, word: str) -> bool:
        traverse = self

        for char in word:
            if char not in traverse.neighbours:
                return False
            
            traverse = traverse.neighbours[char]
        
        return traverse.is_terminating

    def startsWith(self, prefix: str) -> bool:
        traverse = self

        for char in prefix:
            if char not in traverse.neighbours:
                return False
        
            traverse = traverse.neighbours[char]
        
        return traverse.has_prefix
        
        