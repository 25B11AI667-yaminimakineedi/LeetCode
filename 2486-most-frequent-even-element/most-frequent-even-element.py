class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        hashh={}
        for num in nums:
            if num%2==0:
                if num not in hashh:
                    hashh[num]=1
                else:
                    hashh[num]+=1
        if not hashh:
            return -1
        ans=-1
        max_freq=-1
        for key,freq in hashh.items():
            if freq>max_freq:
                max_freq=freq
                ans=key
            elif freq==max_freq:
                if key<ans:
                    ans=key
        return ans



