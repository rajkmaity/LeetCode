class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows,cols= len(grid),len(grid[0])
        grid_sum= [[0]*cols for _ in range(rows)]
        grid_sum[0][0]= grid[0][0]
        for r in range(1,rows):
            grid_sum[r][0]=grid_sum[r-1][0]+grid[r][0]
        for c in range(1,cols):
            grid_sum[0][c]= grid_sum[0][c-1]+ grid[0][c]

        for r in range(1,rows):
            for c in range(1,cols):
                grid_sum[r][c]=grid[r][c]+ min(grid_sum[r-1][c],grid_sum[r][c-1])
        return grid_sum[rows-1][cols-1]


        