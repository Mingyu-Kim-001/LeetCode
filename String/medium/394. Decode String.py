class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        result = ""
        
        def get_num(i):
            result = ""
            while ord("0") <= ord(s[i]) <= ord("9"):
                result += s[i]
                i += 1
            return int(result),i + 1
        
        def rep(i):
            to_repetition = ""
            num,newi = get_num(i)
            i = newi
            while s[i] != "]":
                if ord("0") <= ord(s[i]) <= ord("9"):
                    repeated,newi = rep(i)
                    to_repetition += repeated
                    i = newi
                else:
                    to_repetition += s[i]
                    i += 1
            return to_repetition * num , i + 1
        
        
        while i < len(s):
            
            if ord("0") <= ord(s[i]) <= ord("9"):
                repeated,newi = rep(i)
                result += repeated
                i = newi
            else:
                result += s[i]
                i += 1
        return result