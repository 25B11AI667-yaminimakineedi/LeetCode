class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hashh={}
        for i in stones:
            if i not in hashh:
                hashh[i]=1
            else:
                hashh[i]+=1
        count_jewels=0
        for i in jewels:
            if i in hashh.keys():
                count_jewels+=hashh[i]
        return count_jewels