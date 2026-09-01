class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_array=[]
        sum=0
        for i in nums:
                sum+=i
                sum_array.append(sum)
        return sum_array
    

