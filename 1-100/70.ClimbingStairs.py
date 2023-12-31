class Solution:
    def climbStairs(self, n: int) -> int:
        res=[0]* n
        res[0]=1
        if n==1:
            return 1
        res[1]=2
        for i in range(2,n):
            res[i]=res[i-1]+res[i-2]
        return res[n-1]