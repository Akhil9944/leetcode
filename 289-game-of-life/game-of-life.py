class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return 
        m=len(board)
        n=len(board[0])
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        
        for r in range(m):
            for c in range(n):
                live_neighbors = 0
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        if board[nr][nc] & 1:
                            live_neighbors += 1
                            
                current_state = board[r][c] & 1
                
                if current_state == 1:
                    if live_neighbors == 2 or live_neighbors == 3:
                        board[r][c] |= 2
                else:
                    if live_neighbors == 3:
                        board[r][c] |= 2
                        
        for r in range(m):
            for c in range(n):
                board[r][c] >>= 1