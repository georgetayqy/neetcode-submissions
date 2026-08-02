from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        q = deque()
        wordSet.discard(beginWord)
        q.append(beginWord)
        levels = 0
        seen_words = set()

        while q:
            levels += 1

            for i in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return levels

                if word in seen_words:
                    continue
                seen_words.add(word)

                for neighbour in self.generate_neighbour(word):
                    if neighbour in wordSet:
                        q.append(neighbour)

        return 0

    def generate_neighbour(self, word):
        results = []
        word_ls = list(word)
        initial_char = None

        for i in range(len(word)):
            initial_char = word[i]

            for j in range(26):
                new_char = chr(ord("a") + j)
                if new_char == initial_char:
                    continue

                word_ls[i] = new_char
                results.append("".join(word_ls))

            word_ls[i] = initial_char

        return results
