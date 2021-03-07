class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        def stringToBin(numStr):
            result = 0
            for c in numStr:
                result = result << 1
                result += int(c)
            return result

        MOD = pow(2,k)
        prev = stringToBin(s[:k])
        seen = set()
        seen.add(prev)
        
        for i in range(k,len(s)):
            prev = ((prev<<1) + int(s[i])) % MOD
            seen.add(prev)
            if len(seen) == MOD:
                return True
            
        return False