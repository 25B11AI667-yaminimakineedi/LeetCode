class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashh={}
        for num in nums:
            if num not in hashh:
                hashh[num]=1
            else:
                hashh[num]+=1
        return max(hashh,key=hashh.get)