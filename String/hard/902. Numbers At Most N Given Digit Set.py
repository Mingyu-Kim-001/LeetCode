class Solution:
    def helper(self, digits: List[str], n: str) -> int: 
        res = 0
        int_n = int(n)
        if int_n < 10:
            return len([digit for digit in digits if digit <= n])
        log_10_n = len(n) - 1
        for digit in digits:
            if digit < n[0]:
                res += pow(len(digits), log_10_n)
            elif digit == n[0]:
                res += self.helper(digits, n[1:])
        return res
        
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        log_10_n = len(str(n)) - 1
        return sum([pow(len(digits), order) for order in range(1,log_10_n + 1)]) + self.helper(digits, str(n))
        