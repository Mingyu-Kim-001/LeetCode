#Time: O(2^n)
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy = ["a","b","c"]
        for i in range(1,n):
            happy2 = []
            for word in happy:
                for c in "abc":
                    if word[-1]!=c:
                        happy2.append(word+c)
            happy = happy2
        return happy[k-1] if 1<=k<=len(happy) else ""