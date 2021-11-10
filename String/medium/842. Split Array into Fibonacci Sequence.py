class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        first = 0
        second = 0
        
        def helper(num, first, second, start_idx, ans):
            while start_idx < len(num):
                target = first + second
                if target >= pow(2,31):
                    return False
                for c in str(target):
                    if start_idx >= len(num) or c != num[start_idx]:
                        return False
                    start_idx += 1
                first = second
                second = target
                ans.append(target)
            return True
        
        for i in range(len(num)-2): #first = num[:i+1]
            first *= 10
            first += int(num[i])
            if first >= pow(2, 31):
                break
            for j in range(i+1, len(num)-1): #second = num[i+1:j+1]
                second *= 10
                second += int(num[j])
                if second >= pow(2,31):
                    break
                ans = [first, second]
                if helper(num, first, second, j+1, ans):
                    return ans
                if j == i + 1 and num[j] == "0":
                    break
            second = 0
            if i == 0 and num[0] == "0":
                break
        return []
                