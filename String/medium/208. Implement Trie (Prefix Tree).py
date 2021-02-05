class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        insert_trie = self.trie
        for c in word:
            if not c in insert_trie:
                insert_trie[c] = {}
            insert_trie = insert_trie[c]
        insert_trie["END"] = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        search_trie = self.trie
        for c in word:
            if not c in search_trie:
                return False
            search_trie = search_trie[c]
        return "END" in search_trie
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        search_trie = self.trie
        for c in prefix:
            if not c in search_trie:
                return False
            search_trie = search_trie[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)