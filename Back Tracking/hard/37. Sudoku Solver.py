class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(i,j,num):
            
            #row_check
            for row in range(9):
                if board[row][j] == num:
                    return False
                
            #col_check
            for col in range(9):
                if board[i][col] == num:
                    return False
            
            #block_check
            block_i = 3 * (i // 3)
            block_j = 3 * (j // 3)
            for row in range(3):
                for col in range(3):
                    if board[block_i+row][block_j+col] == num:
                        return False
            
            return True
        
        def solve():
            for i in range(9):
                for j in range(9):
                    
                    if board[i][j] == ".":
                        for num in "123456789":
                            if is_valid(i,j,num):
                                board[i][j] = num
                                if solve():
                                    return True
                        board[i][j] = "."
                        return False
                    
            return True
        
        solve()
            