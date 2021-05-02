class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        
        power_x = []
        power_y = []
        
        if x != 1:
            element = 1
            while element < bound:
                power_x.append(element)
                element *= x
        else:
            power_x = [1]
            
        if y != 1:
            element = 1
            while element < bound:
                power_y.append(element)
                element *= y
        else:
            power_y = [1]
            
        ans = set()
        for i in power_x:
            for j in power_y:
                if i + j <= bound:
                    ans.add(i+j)
        
        return list(ans)
                    