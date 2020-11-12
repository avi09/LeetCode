class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        def find_max_rect(matrix, i, j, rows, cols):
            y = j
            x = i
            max_area = 0
            while y<cols and matrix[i][y]=="1":
                area = 0
                while x<rows and matrix[x][j]=="1":
                    if len(matrix[x][j:y+1]) == matrix[x][j:y+1].count("1"):
                        area+=len(matrix[x][j:y+1])
                    else:
                        break
                    x+=1
                x  = i
                max_area = max(area, max_area)
                y+=1
            return max_area
                
                        
            
        
        if matrix == []:
            return 0
        
        used_points = set()
        rows = len(matrix)
        cols = len(matrix[0])
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]=="1":
                    used_points.add((i,j))
                    tm = find_max_rect(matrix, i, j, rows, cols)
                    if tm>max_area:
                        max_area = tm
        
        return max_area
                        
        
