class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def is_solved(board):
            for i in board:
                if not sorted(i)==["1","2","3","4","5","6","7","8","9"]:
                    return False
            return True
        
        def get_sols(board, i, j):
            that_row = set(board[i])
            that_column = []
            for x in board:
                that_column.append(x[j])
                
            i1 = i-i%3
            j1 = j-j%3
            that_sq = []
            for x in range(i1, i1+3):
                for y in range(j1, j1+3):
                    that_sq.append(board[x][y])
                    
            that_row = that_row.union(set(that_column))
            that_row = that_row.union(set(that_sq)) - {"."}
            
            return {"1", "2", "3", "4", "5", "6", "7", "8", "9"} - that_row
        
        def recurse(board, n):
            if is_solved(board)==True or n==-1:
                n=-1
                print(board)
                return -1
            else:
                for i in range(9):
                    for j in range(9):
                        if board[i][j] == ".":
                            x = get_sols(board, i, j)
                            if len(x)==0:
                                return n
                            for k in x:
                                board[i][j] = k
                                n = recurse(board, n+1)
                                if n == -1:
                                    return -1
                            if n!=0:
                                board[i][j] = "."
                                return n
            return n
        
        board = recurse(board, 0)
        print(board)
        
