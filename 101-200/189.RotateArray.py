class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        if k%n ==0:
            return nums
        k=k%n
        while k>0:
            temp=nums.pop()
            nums.insert(0,temp)
            k-=1