class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(n):
            for j in range(n-1,i,-1):
                sum=nums[i]+nums[j]
                if sum==target:
                    return i,j
                
