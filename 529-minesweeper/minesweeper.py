class Solution(object):
    def updateBoard(self, board, click):
        r, c = click
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board
        
        rows, cols = len(board), len(board[0])
        
        def dfs(x, y):
            if board[x][y] != 'E':
                return
            
            mines = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = x + dr, y + dc
                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'M':
                        mines += 1
            
            if mines > 0:
                board[x][y] = str(mines)
            else:
                board[x][y] = 'B'
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        nr, nc = x + dr, y + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            dfs(nr, nc)
                            
        dfs(r, c)
        return board