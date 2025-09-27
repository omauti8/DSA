class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        def is_valid(r,c,ch):
            for j in range(9):
                if board[r][j]==ch:
                    return False
            for i in range(9):
                if board[i][c]==ch:
                    return False
            srow, scol = 3 * (r // 3), 3 * (c // 3)
            for i in range(srow, srow + 3):
                for j in range(scol, scol + 3):
                    if board[i][j] == ch:
                        return False
            return True

        def back():
            for i in range(9):
                for j in range(9):
                    if board[i][j]=='.':
                        for ch in "123456789":
                            if is_valid(i,j,ch):
                                board[i][j]=ch
                                if back():
                                    return True
                                board[i][j]='.'
                        return False
            return  True
        
        back()
       