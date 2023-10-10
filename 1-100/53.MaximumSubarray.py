class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max=float('-inf')
        a= [0]*len(nums)
        sum=0
        for i in range (len(nums)):
            sum = sum + nums[i]
            global_max = max(global_max,sum)
            sum= max(sum,0)
        return global_max
