class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashh={}
        for i in nums:
            hashh[i]=1
        x=list(hashh.keys())
        for i in range(len(x)):
            nums[i]=x[i]
        return len(x)

        
    

           
        