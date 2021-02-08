class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = []
        for word in words:
            perm = {}
            perm_reverse = {}
            for i,j in zip(pattern,word):
                if perm.get(i)==None and perm_reverse.get(j)==None:
                    perm[i] = j
                    perm_reverse[j] = i
                elif (perm.get(i) and j!=perm[i]) or (perm_reverse.get(j) and i!=perm_reverse[j]):
                    break
            else:
                result.append(word)
        return result