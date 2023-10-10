class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left=0
        m,n= len(matrix),len(matrix[0])
        right = m*n -1 
        def getval(idx):
            i=idx//n
            j=idx-(i*n)
            return(matrix[i][j])

        

        while left<=right:
            mid=(left+right)//2
            if getval(mid)==target:
                return True
            elif getval(mid)>target:
                right=mid-1
            else:
                left=mid+1
        return False