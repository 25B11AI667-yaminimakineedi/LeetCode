class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashh={}
        for num in nums:
            if num not in hashh:
                hashh[num]=1
            else:
                hashh[num]+=1
        top_freq=sorted(hashh,key=hashh.get,reverse=True)
        return top_freq[:k]