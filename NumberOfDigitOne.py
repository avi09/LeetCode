import math
class Solution:
    def countDigitOne(self, n: int) -> int:
        
        if n==0:
            return 0
        n = str(n)
        location = 1
        count = 0
        for i in range(len(n)-1, -1, -1):
            left = n[:i]
            if left=="":
                left = 0
            else:
                left = int(left)
            right = n[i+1:]
            if right=="":
                right = 0
            else:
                right = int(right)
            if n[i]>"1":
                count += (left+1)*location
            elif n[i]=="1":
                count += (left*location) + (right+1)
            else:
                count += (left*location)
            location *= 10
        return count
