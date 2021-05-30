class Solution:
    def maxProduct(self, words: List[str]) -> int:
        alphabet_sets = []
        for word in words:
            alphabet_sets.append(set(word))
        
        ans = 0
        for i in range(len(alphabet_sets)):
            for j in range(i+1,len(alphabet_sets)):
                if not alphabet_sets[i] & alphabet_sets[j]:
                    ans = max(ans, len(words[i])*len(words[j]))
        
        return ans