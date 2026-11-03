class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        q = deque()
        l = len(beginWord)
        visited = set()
        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        neighbor = defaultdict(list)

        for word in wordList:
            for i in range(l):
                subword = word[:i] + "*" + word[i+1:]
                neighbor[subword].append(word)

        q.append((beginWord,1))

        while q:
            word, jumps = q.popleft()


            if word == endWord:
                return jumps

            for i in range(l):
                subword = word[:i] + "*" + word[i+1:]
                if subword in neighbor:
                    for nei in neighbor[subword]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append((nei,jumps+1))

        return 0