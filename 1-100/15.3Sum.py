lass Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        n= len(nums)
        for i in range(n-2):
            j=i+1
            k=n-1
            
            sol=[]
            while j<k:
                totalsum=nums[i]+nums[j]+nums[k]
                if totalsum==0:
                    sol=[nums[i],nums[j],nums[k]]
                    if sol not in res:
                        res.append(sol) 
                    
                    j+=1
                    k-=1
                elif totalsum >0:
                    k-=1
                else:
                    j+=1
        return res

