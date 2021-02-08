class Solution:
    def printVertically(self, s: str):
        words = s.split(" ")
        
        maxWordLen = max([len(word) for word in words])
        result = []
        for i in range(maxWordLen):
            verticalWord = ""
            temp = ""
            for word in words:
                if i<len(word):
                    temp+=word[i]
                    verticalWord+=temp
                    temp=""
                else:
                    temp+=" "
            result.append(verticalWord)
        return result