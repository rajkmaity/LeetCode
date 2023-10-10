class Solution:
    def trap(self, height: List[int]) -> int:
        left_side=[0]*len(height)
        right_side=[0]*len(height)
        max_left=0
        for i in range(1,len(height)):
            max_left=max(max_left,height[i-1])
            left_side[i]=max_left
        max_right=0
        for i in range(len(height)-2,-1,-1):
            max_right= max(max_right,height[i+1])
            right_side[i]=max_right
        total_water=0
        for i in range(len(height)):
            total_water+= max(0,min(left_side[i],right_side[i])-height[i])
        return total_water

        