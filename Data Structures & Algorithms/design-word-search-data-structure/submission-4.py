class WordDictionary:

    def __init__(self, is_terminating: bool = False):
        self.characters = {}
        self.is_terminating = is_terminating

    def addWord(self, word: str) -> None:
        iterator = self

        for char in word:
            iterator.characters[char] = iterator.characters.get(
                char,
                WordDictionary()
            )
            iterator = iterator.characters[char]
        
        iterator.is_terminating = True

    def search(self, word: str) -> bool:
        def iterator(index, node):
            if index >= len(word):
                return node.is_terminating

            if word[index] == ".":
                it = False

                for char in node.characters:
                    it = iterator(index + 1, node.characters[char]) or it

                return it
            else:
                c = word[index]

                if c not in node.characters:
                    return False

                return iterator(index + 1, node.characters[c])
                    
        return iterator(0, self)
