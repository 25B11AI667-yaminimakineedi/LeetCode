class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        total=sum=0
        for i in nums:
            total+=i
            while i>0:
                sum+=i%10
                i=i//10
        return abs(total-sum)
        
