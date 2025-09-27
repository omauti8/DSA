class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        col=len(board[0])

        def back(r,c,index):
            if index== len(word):
                return True
            if r<0 or c<0 or r>= rows or c>= col or board[r][c]!= word[index]:
                return False

            temp = board[r][c]
            board[r][c]="*"

            found=(back(r+1,c,index+1)or
                    back(r-1,c,index+1) or
                    back(r,c+1,index+1) or
                    back(r,c-1,index+1))

            board[r][c]= temp
            return found

        for r in range(rows):
            for c in range(col):
                if back(r,c,0):
                    return True
        
        return False
