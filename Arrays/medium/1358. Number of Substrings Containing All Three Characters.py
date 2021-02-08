class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counter = {"a":0,"b":0,"c":0}
        start_num = 0
        curr_num = 0
        result = 0
        counter[s[0]]=1
        while curr_num<len(s)-1:
            if counter["a"]==0 or counter["b"]==0 or counter["c"]==0:
                curr_num+=1
                counter[s[curr_num]]+=1
            
            while counter["a"]!=0 and counter["b"]!=0 and counter["c"]!=0:
                counter[s[start_num]]-=1
                start_num+=1
                result+= len(s) - curr_num
                
        return result