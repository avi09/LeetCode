class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        def run(s1, s2, s3, i, found, cache):
            if s1+s2==s3[i:]:
                found = True
                return found
            if (s1,s2) in cache:
                found = False
                return found
            if i==len(s3)-1:
                if s1=="" and s2=="":
                    found = True
                    return found
                else:
                    cache.add((s1, s2))
                    found = False
                    return found
                    
            if s3[i+1]==s1[:1]:
                found = run(s1[1:], s2, s3, i+1, found, cache)
                if found:
                    return found
                
            if s3[i+1]==s2[:1]:
                found = run(s1, s2[1:], s3, i+1, found, cache)
                return found
                
        if len(s1+s2)==len(s3):
            found = run(s1, s2, s3, -1, False, set())
            return found
        return False
