class Solution:
    def reverseWords(self, s: str) -> str:
        s1=s.split()
        res=s1[-1]
        for i in range(len(s1)-2,-1,-1):
            res+=" "+s1[i]

        return res