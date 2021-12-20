class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def row_check(board):
            for i in range(9):
                row_numbers = set()
                for j in range(9):
                    if board[i][j] == ".":
                        continue
                    if not board[i][j] in row_numbers:
                        row_numbers.add(board[i][j])
                    else:
                        return False
            return True
        
        def col_check(board):
            for j in range(9):
                col_numbers = set()
                for i in range(9):
                    if board[i][j] == ".":
                        continue
                    if not board[i][j] in col_numbers:
                        col_numbers.add(board[i][j])
                    else:
                        return False
            return True
        
        def square_check(board):
            for i in range(3):
                for j in range(3):
                    square_numbers = set()
                    for k in range(3):
                        for l in range(3):
                            if board[3*i+k][3*j+l] == ".":
                                continue
                            if not board[3*i+k][3*j+l] in square_numbers:
                                square_numbers.add(board[3*i+k][3*j+l])
                            else:
                                return False
            return True
        return row_check(board) and col_check(board) and square_check(board)
                            