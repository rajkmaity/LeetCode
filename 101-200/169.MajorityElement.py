class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=1
        select=nums[0]
        for i in range(1,len(nums)):
            if select == nums[i]:
                count+=1
            else:
                if count >0:
                    count-=1
                else:
                    count=1
                    select=nums[i]
        return select
