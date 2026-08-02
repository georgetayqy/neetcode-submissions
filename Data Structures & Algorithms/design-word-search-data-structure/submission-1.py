class WordDictionary:
    def __init__(self):
        self.isTerminating = False
        self.neighbours = {}

    def addWord(self, word: str) -> None:
        """Usual Trie addition"""

        iterator = self

        for char in word:
            if char not in iterator.neighbours:
                iterator.neighbours[char] = WordDictionary()
            
            iterator = iterator.neighbours[char]
    
        iterator.isTerminating = True

    def search(self, word: str) -> bool:
        # Stack to hold tuples of the form (index, node), where 'index' is the current
        # position in the word, and 'node' is the current Trie node.
        stack = [(0, self)]

        # While there are elements in the stack
        while stack:
            # Pop the top element
            index, node = stack.pop()

            # Iterate from the current index to the end of the word
            for i in range(index, len(word)):
                current = word[i]

                # If it is a wildcard, we need to explore all possible neighbours
                if current == ".":
                    # Push all neighbours to the stack with the next index
                    for neighbour in node.neighbours.values():
                        stack.append((i + 1, neighbour))
                    # Since '.' can match any character, continue to the next iteration
                    # IMPORTANT, BREAK HERE DO NOT CONTINUE SEARCHING THE WORD
                    break
                else:
                    # If the character is not in the current node's neighbours, it's a mismatch
                    # IMPORTANT: BREAK HERE TO PREVENT EXPLORING FURTHER (TERMINATE THE SEARCH
                    # HERE)
                    if current not in node.neighbours:
                        break
                    
                    # Move to the next node in the Trie
                    node = node.neighbours[current]
            # FOR ELSE LOOP
            # !!!
            # ELSE EXECUTES AT THE END OF A LOOP IF THE LOOP IS EXECUTED TO COMPLETION WITHOUT]
            # BREAKING
            # !!!
            else:
                # If we completed the for loop without breaking, check if we are at a terminating node
                if node.isTerminating:
                    return True
        
        # If we exhausted the stack without finding a match, return False
        return False

