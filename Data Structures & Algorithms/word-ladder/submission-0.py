from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        mapping = {}

        wordList.append(beginWord)
        for word in wordList:
            for word2 in wordList:
                if word == word2:
                    continue

                delta = 0
                for i in range(len(word)):
                    if word[i] != word2[i]:
                        delta += 1
                
                if delta == 1:
                    mapping[word] = mapping.get(word, set())
                    mapping[word].add(word2)
                    mapping[word2] = mapping.get(word2, set())
                    mapping[word2].add(word)
        wordList.pop()

        q = deque()
        q.append([beginWord, 1])
        seen = set()
        print(mapping)

        while q:
            for i in range(len(q)):
                word, count = q.popleft()

                if word == endWord:
                    return count
                
                if word in seen:
                    continue
                
                seen.add(word)

                for target in mapping.get(word, []):
                    q.append([target, count + 1])
        
        return 0
        