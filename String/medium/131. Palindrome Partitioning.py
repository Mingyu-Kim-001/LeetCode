class Solution:
    def isPalindrome(self,someStr):
        return all(someStr[i]==someStr[len(someStr)-1-i] for i in range(len(someStr)))
    def partition(self, s: str) -> List[List[str]]:
        if len(s)==1: return [[s]]
        result = [] if not self.isPalindrome(s) else [[s]]
        for i in range(len(s)-1,0,-1):
            if self.isPalindrome(s[i:]):
                a = self.partition(s[:i])
                for j in a:
                    result.append(j+[s[i:]])
        return result