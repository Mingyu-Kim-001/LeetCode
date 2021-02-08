class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def decomp(word):
            result = []
            i = 0
            while i<len(word):
                element = []
                prevI = i
                while i<len(word)-1 and word[i]==word[i+1]: 
                    i+=1
                element = [word[prevI],i-prevI+1]
                result.append(element)
                i+=1
            return result
        SDecomp = decomp(S)
        result = 0
        for word in words:
            wordDecomp = decomp(word)
            if len(SDecomp)==len(wordDecomp):
                for sElement,wElement in zip(SDecomp,wordDecomp):
                    if sElement[0]!= wElement[0] or not(sElement[1]==wElement[1] or (sElement[1]>=3 and sElement[1]>=wElement[1])):
                        break
                else:
                    result+=1
        return result