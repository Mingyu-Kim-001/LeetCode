class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        shifts[-1] %= 26
        for i in range(len(shifts)-2, -1, -1):
            shifts[i] += shifts[i+1]
            shifts[i] %= 26
        ans = ""
        for i, c in enumerate(s):
            ans += chr((ord(c) - ord('a') + shifts[i]) % 26 + ord('a'))
        
        return ans