from collections import defaultdict
class Solution:
    def __init__(self):
        self.chain_len = None
        
    def DFS(self, word):
        if self.chain_len[word] > 1:
            return self.chain_len[word]
        
        for i in range(len(word)+1):
            for c in "abcdefghijklmnopqrstuvwxyz":
                new_word = word[:i] + c + word[i:]
                if new_word in self.chain_len:
                    self.chain_len[word] = max(self.chain_len[word], self.DFS(new_word) + 1)
        
        return self.chain_len[word]
                    
    def longestStrChain(self, words: List[str]) -> int:
        self.chain_len = {word : 1 for word in words}
        
        for word in words:
            self.DFS(word)
            
        return max(self.chain_len.values())
        