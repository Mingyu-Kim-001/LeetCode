class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = {}
        self.words_to_trie(words)
        self.max_word_length = max([len(word) for word in words])
        self.stream = ""
        
    def words_to_trie(self, words):
        for word in words:
            cur = self.trie
            for char in word[::-1]:
                if not char in cur:
                    cur[char] = {}
                cur = cur[char]
            cur["END"] = None
            

    def query(self, letter: str) -> bool:
        self.stream = (letter + self.stream)[:self.max_word_length]
        cur = self.trie
        for char in self.stream:
            if "END" in cur:
                return True
            if not char in cur:
                return False
            cur = cur[char]
        return "END" in cur
        
        
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)