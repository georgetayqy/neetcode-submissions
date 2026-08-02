class PrefixTree:

    def __init__(self):
        self.is_terminating = False
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        iterator = self.head

        for i in range(len(word)):
            curr_char = word[i]

            if not iterator.hasNeighbour(curr_char):
                iterator.addNode(curr_char, False)

            iterator = iterator.getNeighbour(curr_char)
            
            if i == len(word) - 1:    
                iterator.is_terminating = True    

    def search(self, word: str) -> bool:
        iterator = self.head

        for i in range(len(word)):
            curr_char = word[i]
            
            if not iterator.hasNeighbour(curr_char):
                return False
            
            iterator = iterator.getNeighbour(curr_char)
            
            if i == len(word) - 1 and not iterator.is_terminating:
                return False
        
        return True

    def startsWith(self, prefix: str) -> bool:
        iterator = self.head

        for i in range(len(prefix)):
            curr_char = prefix[i]

            if not iterator.hasNeighbour(curr_char):
                return False
            
            iterator = iterator.getNeighbour(curr_char)

        return True
        

class TrieNode:
    def __init__(self, char = None, isTerminating = False):
        self.is_terminating = isTerminating
        self.neighbours = {char: self} if char else {}
    
    def addNode(self, char, isTerminating):
        assert char not in self.neighbours

        self.neighbours[char] = TrieNode(char, isTerminating)

    def getNeighbour(self, char):
        assert char in self.neighbours
        return self.neighbours[char]

    def hasNeighbour(self, char):
        return char in self.neighbours    
