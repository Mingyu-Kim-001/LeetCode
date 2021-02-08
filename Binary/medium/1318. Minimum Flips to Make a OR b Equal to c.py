class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        c_bits = bin(c)[2:]
        a_bits = bin(a)[2:]
        b_bits = bin(b)[2:]
        maxLen = max(len(c_bits),len(a_bits),len(b_bits))
        a_bits,b_bits,c_bits = [i.zfill(maxLen) for i in [a_bits,b_bits,c_bits]]
        result = 0
        #print(a_bits,b_bits,c_bits)
        for a_bit,b_bit,c_bit in zip(a_bits,b_bits,c_bits):
            #print(a_bit,b_bit,c_bit)
            if c_bit=="1":
                if not (a_bit=="1" or b_bit=="1"):
                    result+=1
            else:
                result+= (a_bit=="1") + (b_bit=="1")
            #print(result)
        return result