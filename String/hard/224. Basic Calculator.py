class Solution:
    def calculate(self, s: str) -> int:
        parse_index = 0
        
        def operation(op1, op2, operator):
            if operator == "+":
                return op1 + op2
            return op1 - op2
        
        def calculate_helper(parse_index):
            op1 = 0
            op2 = "0"
            previous_operator = "+"
            while parse_index < len(s):
                if s[parse_index] == ")":
                    return operation(op1, int(op2), previous_operator), parse_index
                elif s[parse_index] in ("+", "-"):
                    op1 = operation(op1, int(op2), previous_operator)
                    op2 = "0"
                    previous_operator = s[parse_index]
                elif s[parse_index] == "(":
                    op2, parse_index = calculate_helper(parse_index+1)
                elif s[parse_index] != " ":
                    op2 += s[parse_index]
                parse_index += 1
                
            return operation(op1, int(op2), previous_operator), len(s)
        
        return calculate_helper(0)[0]