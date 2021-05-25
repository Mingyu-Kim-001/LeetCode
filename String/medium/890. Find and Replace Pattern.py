class Solution:
    def normalize_word(self,word):
        result = ""
        change = {}
        for i,p in enumerate(word):
            if not p in change:
                change[p] = chr(ord("A")+len(change))
            result += change[p]
        return result
    
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        pattern_normalized = self.normalize_word(pattern)
        ans = []
        for word in words:
            if self.normalize_word(word) == pattern_normalized:
                ans.append(word)
        return ans