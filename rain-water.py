class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        if sum(height) == 0:
            return 0
        s = sum(height)
        for i in range(1, max(height)+1):
            
            while height[0]<i:
                height = height[1:]
                
            while height[::-1][0]<i:
                height = height[:len(height)-1]
                
            total+=len(height)
            
                    
        return total - s
