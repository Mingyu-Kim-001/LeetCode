#Time:O(n)
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        result = []
        for i in S:
            if i=="(":
                result.append(i)
            else:
                if result[-1]=="(":
                    result.pop()
                    num = 1
                else:
                    num = result.pop()
                    num*=2
                    result.pop()
                if not result or result[-1]=="(":
                    result.append(num)
                else:
                    result[-1]+=num
        return result[0]