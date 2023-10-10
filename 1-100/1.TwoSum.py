class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        remainder = target-nums[0]
        dict[remainder]=0
        print(dict)
        L=len(nums)
        for i in range (1,L) :
            remainder=target-nums[i]
            if  nums[i] in dict:
                return [dict[nums[i]],i]
            else:
                dict[remainder]=i