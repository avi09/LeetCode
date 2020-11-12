import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        answer = ""
        candidates = list(range(1, n+1))
        i = int(n)
        while len(answer)!=n:
            fetch_1 = int( math.ceil( k/( (math.factorial(i)/i) ) ) - 1 )
            answer+=str(candidates[fetch_1])
            candidates.pop(fetch_1)
            k-=int(((fetch_1+1)*(math.factorial(i)/i)))
            i-=1
        
        return answer
            
