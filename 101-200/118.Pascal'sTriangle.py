class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        def createrow(l):
            res=[]
            res.append(1)
            for i in range(len(l)-1):
                res.append(l[i]+l[i+1])
            res.append(1)
            return res
        pascal=[]
        
        if numRows==0:
            return pascal
        pascal.append([1])
        
        for r in range(2,numRows+1):
            pascal.append(createrow(pascal[-1]))
        return pascal
        