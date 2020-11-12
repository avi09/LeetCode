class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if s=="" or s==".": 
            return False
        
        valid = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "e", ".", "-", "+"]
        for i in range(len(s)):
            if s[i] not in valid:
                return False
            if i==0:
                if s[i] in ["e"]:
                    return False
                if s.count(".")>1 or s.count("e")>1:
                    return False
                if s.find("e")<s.find(".") and s.find("e")!=-1 and s.find(".")!=-1:
                    return False
                if s[i]==".":
                    if len(s)==0:
                        return False
                    if not s[i+1].isdigit():
                        return False
            elif i==len(s)-1:
                if s[i] in ["e","+","-"]:
                    return False
                if s[i-1]=="." and s[i]==".":
                    return False
                if s[i]==".":
                    if len(s)==1:
                        return False
                    if not s[i-1].isdigit():
                        return False
            elif s[i] == "+":
                if s[i-1] in ["+","-","."]:
                        return False
                if s[i+1].isdigit() and s[i-1].isdigit():
                    return False
            elif s[i] == "-":
                if s[i-1] in ["+","-","."]:
                        return False
                if s[i+1].isdigit() and s[i-1].isdigit():
                    return False
            elif s[i] == "e":
                if s[i-1] in ["+","-"]:
                    return False
                if s[i+1] in ["."]:
                    return False
            elif s[i] == ".":
                if (s[i+1] in ["+","-","."]) or (s[i-1] in ["e","."]):
                    return False
                
        
        return True
        
