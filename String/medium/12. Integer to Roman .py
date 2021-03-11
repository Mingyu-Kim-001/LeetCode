class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {0:"",1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VII",9:"IX",10:"X",50:"L",100:"C",500:"D",1000:"M"}
        result = ""
        for i in range(3,-1,-1):
            power = pow(10,i)
            each_num = num // power
            num = num % power
            if each_num in (1,2,3):
                result += roman[power] * each_num
            elif each_num == 4:
                result +=  roman[power] + roman[power*5]
            elif each_num in (5,6,7,8):
                result += roman[power*5] + roman[power] * (each_num-5)
            elif each_num == 9:
                result += roman[power] + roman[power*10]
        return result
                