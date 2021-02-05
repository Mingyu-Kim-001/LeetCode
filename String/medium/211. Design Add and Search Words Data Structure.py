class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        if not word: return
        addTrie = self.trie
        for c in word:
            if not c in addTrie:
                addTrie[c] = {}
            addTrie = addTrie[c]
        addTrie["END"] = True
        # print(self.trie)
        
    def search(self, word: str) -> bool:
        # print(word)
        if word=="":
            return True
        def searchHelper(word,eachTrie):
            if word=="": 
                return ("END" in eachTrie)
            for i,c in enumerate(word):
                if c==".":
                    for c2 in eachTrie:
                        if c2!="END" and searchHelper(word[i+1:],eachTrie[c2]):
                            return True
                    return False
                else:
                    if c in eachTrie:
                        eachTrie = eachTrie[c]
                    else:
                        return False
            return ("END" in eachTrie)
        return searchHelper(word,self.trie)
                    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)