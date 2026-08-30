class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
       freq={}
       for n in nums:
            if n in freq:
                freq[n]+=1
            else:
                freq[n]=1
       for key in freq:
            if freq[key]>=2:
                return True
       return False