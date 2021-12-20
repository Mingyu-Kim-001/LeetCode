class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = (num1, num2) if len(num1) <= len(num2) else (num2, num1)
        
        carry = 0
        nums = []
        for i in range(1, len(num1)+1):
            n1, n2 = num1[-i], num2[-i]
            result = str((int(n1) + int(n2) + carry) % 10)
            carry = (int(n1) + int(n2) + carry) // 10
            nums.append(result)
            
        for i in range(len(num1)+1, len(num2)+1):
            result = str((int(num2[-i]) + carry) % 10)
            carry = (int(num2[-i]) + carry) // 10
            nums.append(result)
        
        if carry:
            nums.append("1")
        
        return "".join(nums)[::-1]
            
        