class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
       hashh={}
       for num in nums:
            if num not in hashh:
                hashh[num]=1
            else:
                hashh[num]+=1
       target=len(nums)//3 
       x=[]
       for key, value in hashh.items():
        if value>target:
            x.append(key)
       return x



