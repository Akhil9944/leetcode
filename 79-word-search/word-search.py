class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        ROWS, COLS = len(board), len(board[0])
        
        if len(word) > ROWS * COLS:
            return False
            
        
        board_counts = {}
        for r in range(ROWS):
            for c in range(COLS):
                char = board[r][c]
                board_counts[char] = board_counts.get(char, 0) + 1
                
        for char in word:
            if board_counts.get(char, 0) < word.count(char):
                return False

        
        if board_counts[word[0]] > board_counts[word[-1]]:
            word = word[::-1]

        def dfs(r, c, i):
            if i == len(word):
                return True
                
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                board[r][c] != word[i]):
                return False
            
            
            temp = board[r][c]
            board[r][c] = '#'
            
            
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            
            board[r][c] = temp
            
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
                        
        return False