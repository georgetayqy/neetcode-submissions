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
        def dfs(index, iterator):
            # iterate from the current index to the end of the word
            # we need to apply backtracking and and use DFS here
            for i in range(index, len(word)):
                # get the current word first
                current = word[i]

                # if it is a wildcard
                if current == ".":
                    # recursively call dfs on all neighbouring values since they are all
                    # possible candidates for the search
                    for neighbour in iterator.neighbours.values():
                        # if the DFS returns true, then we just return True here
                        # can imagine reaching further and further into the Trie until
                        # we reach the base case where we can no longer explore further
                        # (word is exhausted) and we return if this node is actually
                        # a terminating node
                        if dfs(i + 1, neighbour):
                            # return True here directly, no need to descend any further as
                            # we have found a candidate
                            return True
                    
                    # if there are no such Trie branch that leads to a valid query for the
                    # string, then we return False
                    return False
                else:
                    # if current is not in the iterator's neighbours, then we have found a
                    # mismatch, so we terminate DFS and return False
                    if current not in iterator.neighbours:
                        return False
                    
                    # we advance the DFS to the next node if it exists
                    iterator = iterator.neighbours[current]
            
            # if we exited the loop, means that we reached a base case where there is no
            # further elements
            return iterator.isTerminating
        
        # run DFS
        return dfs(0, self)
