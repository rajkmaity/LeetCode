class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        a= [0]*n
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        a[0]=nums[0]
        a[1]=max(nums[0],nums[1])
        for i in range(2,n):
            a[i]= max(a[i-1],nums[i]+a[i-2])

        return max(a)