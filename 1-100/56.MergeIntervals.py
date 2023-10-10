class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<=1:
            return intervals
        intervals.sort()
        res=[]
        res.append(intervals[0])
        for i in range(1,len(intervals)):
            prev=res.pop()
            prev_right=prev[1]
            left=intervals[i][0]
            right=intervals[i][1]
            if prev_right<left:
                res.append(prev)
                res.append(intervals[i])
            else:
                if prev_right<=right:
                    prev[1]=right
                res.append(prev)

        return res