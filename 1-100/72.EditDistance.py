class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1=len(word1)+1
        len2=len(word2)+1
        dp=[[-1 for j in range(len2)] for j in range(len1)]
        #if i become 0 then return j
        #if j become 0 then return i 
        for i in range(len1):
            for j in range(len2):
                if i==0:
                    dp[i][j]=j
                elif j==0:
                    dp[i][j]=i
                #if there is a match between them
                #return the diagonal element
                elif word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                #otherwise take min of diagnol,upper and left element 
                #and add 1 to it
                    dp[i][j]=1+min(dp[i-1][j],min(dp[i-1][j-1],dp[i][j-1]))
        return dp[len1-1][len2-1]