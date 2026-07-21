class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n=len(nums)
        count=0
        for i in range(n):
            for j in range(n-1,i,-1):
                sum=nums[i]+nums[j]
                if sum<target:
                    count+=1
        return count
