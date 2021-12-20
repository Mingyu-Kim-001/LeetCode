class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        if n == 1:
            return [1]
        even_len = n // 2
        odd_len = n - even_len
        return [2*i-1 for i in self.beautifulArray(odd_len)] + [2*i for i in self.beautifulArray(even_len)]