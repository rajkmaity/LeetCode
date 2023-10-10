class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1:
            return 1
        if x<1:
            return 0
        
        count=0
        i=1
        while x>0:
            x-=i
            i+=2
            count+=1
            if x==0:
                return count
        return count-1