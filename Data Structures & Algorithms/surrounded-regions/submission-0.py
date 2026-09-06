class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        def capture(i,j):
            if i<0 or i>=ROWS or j <0 or j>=COLS or board[i][j] != 'O':
                return

            if board[i][j] == 'O':
                board[i][j] ='T'
            capture(i+1,j)
            capture(i-1,j)
            capture(i,j+1)
            capture(i,j-1)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O' and (i in [0,ROWS-1] or j in [0,COLS-1]):
                    capture(i,j)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'T':
                    board[i][j] = 'O'

