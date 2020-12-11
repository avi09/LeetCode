class Solution:
    def minCut(self, s: str) -> int:
        
        if s==s[::-1]:
            return 0
        cuts=0
        i = 0
        while i<len(s):
            j = len(s)-1
            while j>=i:
                if s[i:j+1]==s[i:j+1][::-1]:
                    i = j + 1
                    break
                j-=1
            print(i,j)
            if i==j+1 and i<len(s)+1:
                cuts+=1
                
        cuts1=cuts-1
        cuts = 0
        i = len(s)-1
        while i>=0:
            j = 0
            while j<=i:
                if s[j:i+1]==s[j:i+1][::-1]:
                    i = j - 1
                    break
                j+=1
            print(i,j)
            if i==j-1 and i>=-1:
                cuts+=1
        return min(cuts1, cuts-1)
