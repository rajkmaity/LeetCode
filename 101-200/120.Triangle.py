class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m=len(triangle)
        summ= [[0]*(i+1) for i in range(m)]
        summ[0][0]=triangle[0][0]
        if m==1:
            return triangle[0][0]

        for i in range(1,m):
            summ[i][0]=summ[i-1][0]+triangle[i][0]
            for j in range(1,i):
                summ[i][j]= min(summ[i-1][j],summ[i-1][j-1])+triangle[i][j]
            summ[i][i]=summ[i-1][i-1]+triangle[i][i]
        return min(summ[m-1])
                
