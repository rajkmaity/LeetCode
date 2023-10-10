class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[n]*n
        dp[0]=0
        for i in range(1,n):
            for j in range(i):
                if i-j<=nums[j]:
                    dp[i]=min(dp[j]+1,dp[i])
        return dp[-1]
        