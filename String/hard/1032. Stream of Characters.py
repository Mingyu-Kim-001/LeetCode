class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = {}
        self.words_to_trie(words)
        # print(self.trie)
        self.queue = []
        
    def words_to_trie(self, words):
        for word in words:
            cur = self.trie
            for char in word:
                if not char in cur:
                    cur[char] = {}
                cur = cur[char]
            cur["END"] = None
            

    def query(self, letter: str) -> bool:
        self.queue = [trie[letter] for trie in self.queue if letter in trie]
        if letter in self.trie:
            self.queue.append(self.trie[letter])
        return any(["END" in trie for trie in self.queue])
        
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)