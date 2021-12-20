# Time: worst case O(2^n), space: O(2^n)
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        result = [S]
        for i,c in enumerate(S):
            if c.isalpha():
                curLen = len(result)
                for j in range(curLen):
                    s = result[j]
                    result.append(s[:i] + 
                                  (c.upper() if c.islower() else c.lower()) + 
                                  s[i+1:]
                                 )
        return result