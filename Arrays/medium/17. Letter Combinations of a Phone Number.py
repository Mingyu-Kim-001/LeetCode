class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        num_to_alphabet = {"2":["a","b","c"],
                           "3":["d","e","f"],
                           "4":["g","h","i"],
                           "5":["j","k","l"],
                           "6":["m","n","o"],
                           "7":["p","q","r","s"],
                           "8":["t","u","v"],
                           "9":["w","x","y","z"]
                          }
        result = num_to_alphabet[digits[0]]
        for i in range(1,len(digits)):
            result2 = []
            for j in range(len(result)):
                for c in num_to_alphabet[digits[i]]:
                    result2.append(result[j]+c)
            result = result2
        return result