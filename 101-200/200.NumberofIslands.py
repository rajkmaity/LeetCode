class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]=='0' or visited[i][j]:
                return
            visited[i][j]=True
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        
        if not grid:
            return 0


        m,n= len(grid),len(grid[0])
        visited= [[False]*n for _ in range(m)]

        num_islands=0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    dfs(i,j)
                    num_islands+=1
        return num_islands