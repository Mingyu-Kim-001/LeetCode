class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = 0
        for c1 in num1:
            sub_product = 0
            for c2 in num2:
                sub_product *= 10
                sub_product += (ord(c1) - ord('0')) * (ord(c2) - ord('0'))
            ans *= 10
            ans += sub_product
        return str(ans)