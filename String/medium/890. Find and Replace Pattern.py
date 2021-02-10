class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = []
        for word in words:
            match = {}
            match_reverse = {}
            for i,j in zip(word,pattern):
                if i in match or j in match_reverse:
                    if not (i in match and j in match_reverse) or (match[i]!=j or match_reverse[j]!=i):
                        break
                else:
                    match[i] = j
                    match_reverse[j] = i
            else:
                result.append(word)
        return result