class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        arr=[]
        for i in nums:
            count_digits=0
            while i>0:
                digit=i%10
                count_digits+=1
                i=i//10
            if count_digits % 2==0:
                arr.append(i)
        return len(arr)

