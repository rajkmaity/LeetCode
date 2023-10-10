class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        vis = set()

        def dfs(r, c, cur):
            if cur == len(word):
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or word[cur] != board[r][c] or (r, c) in vis:
                return False
            
            vis.add((r, c))

            check = (dfs(r + 1, c, cur + 1) or
                    dfs(r - 1, c, cur + 1) or
                    dfs(r, c + 1, cur + 1) or
                    dfs(r, c - 1, cur + 1))
                    
            vis.remove((r, c))

            return check
        
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        return False