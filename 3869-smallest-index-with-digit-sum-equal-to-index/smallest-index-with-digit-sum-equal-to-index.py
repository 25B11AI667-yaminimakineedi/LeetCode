class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        indices=[]
        for i in range(len(nums)):
            sum=0
            x=nums[i]
            while x>0:
                dig=x%10
                sum+=dig
                x=x//10
            if i==sum:
                    return i
        return -1
