class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1_real, num1_img = int(num1.split("+")[0]), int(num1.split("+")[1][:-1])
        num2_real, num2_img = int(num2.split("+")[0]), int(num2.split("+")[1][:-1])
        result_real = num1_real * num2_real - num1_img * num2_img
        result_img = num1_real * num2_img + num1_img * num2_real
        return str(result_real) + "+" + str(result_img) + "i"