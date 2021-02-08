class Solution:
    def modifyString(self, s: str) -> str:
        if len(s)==0: return s
        if len(s)==1: return s if s!="?" else "a"
        for i,c in enumerate(s):
            if c=="?":
                if i==0:
                    s = ("a" if s[i+1]!="a" else "b") + s[(i+1):]
                elif i==len(s)-1:
                    s = s[:i] + ("a" if s[i-1]!="a" else "b")
                else:
                    if s[i+1]=="a":
                        s = s[:i] + ("b" if s[i-1]!="b" else "c") + s[(i+1):]
                    elif s[i-1]=="a":
                        s = s[:i] + ("b" if s[i+1]!="b" else "c") + s[(i+1):]
                    else:
                        s = s[:i] + "a" + s[(i+1):]
        return s
                        
                