class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        alphabet = []
        not_alphabet = []
        for c in s:
            if ord("a") <= ord(c) <= ord("z") or ord("A") <= ord(c) <= ord("Z"):
                alphabet.append(c)
            else:
                not_alphabet.append(c)
                
        not_alphabet = not_alphabet[::-1]
        result = ""
        for c in s:
            if ord("a") <= ord(c) <= ord("z") or ord("A") <= ord(c) <= ord("Z"):
                result += alphabet.pop()
            else:
                result += not_alphabet.pop()
        
        return result